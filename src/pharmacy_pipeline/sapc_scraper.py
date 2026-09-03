import re
import string
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from bs4 import BeautifulSoup

BASE_URL   = "https://interns.pharma.mm3.co.za"
SEARCH_URL = f"{BASE_URL}/SearchRegister"
DETAIL_URL = f"{BASE_URL}/SearchRegister/OrganisationSearchDetail"

PROVINCES = {"Gauteng": "3", "KwaZulu-Natal": "4"}
CHARS     = string.ascii_uppercase
MIN_CHARS = 3     # server-enforced search minimum
RESULT_CAP = 100  # a full page with no next link means the prefix must be expanded

DETAIL_FIELD_MAP = {
    "account number":         "y_number",
    "pharmacy name":          "pharmacy_name",
    "name":                   "pharmacy_name",
    "license number":         "licence_number",
    "licence number":         "licence_number",
    "doh conditions":         "doh_conditions",
    "registration date":      "registration_date",
    "status":                 "status",
    "owner":                  "owner",
    "responsible pharmacist": "responsible_pharmacist",
    "tutor(s)":               "tutors",
    "inspection":             "inspection",
    "province":               "province",
    "city":                   "city",
    "street address":         "street_address",
    "tel":                    "telephone",
    "provision":              "provision",
}

_DETAIL_ID_RE = re.compile(r"OrganisationSearchDetail/(\d+)", re.I)
_PAGER_RE     = re.compile(r"pager|pagination", re.I)
_NEXT_RE      = re.compile(r"next|>", re.I)


def make_session():
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/149.0",
        "Origin":  BASE_URL,
        "Referer": SEARCH_URL,
    })
    return session


def warmup_and_token(session):
    """Prime the session and return the CSRF token required for search POSTs."""
    resp = session.get(SEARCH_URL, timeout=15)
    soup = BeautifulSoup(resp.text, "lxml")
    inp  = soup.find("input", {"name": "__RequestVerificationToken"})
    return inp["value"] if inp else None


def post_search(session, province_id, text, token):
    fields = {
        "OnlineSearchTypeId":         "2",
        "ProvinceId":                 province_id,
        "SearchText":                 text,
        "__RequestVerificationToken": token or "",
    }
    try:
        return session.post(SEARCH_URL,
                            files={k: (None, v) for k, v in fields.items()},
                            timeout=20)
    except requests.RequestException:
        return None


def parse_table(html):
    """Return (row dicts, has_next_page) from a search results page."""
    soup  = BeautifulSoup(html, "lxml")
    table = soup.find("table")
    if not table:
        return [], False
    all_tr = table.find_all("tr")
    if len(all_tr) < 2:
        return [], False

    headers = [th.get_text(strip=True) for th in all_tr[0].find_all(["th", "td"])]
    rows = []
    for tr in all_tr[1:]:
        cells = tr.find_all("td")
        if not cells:
            continue
        row = {headers[i]: cells[i].get_text(separator=" ", strip=True)
               for i in range(min(len(headers), len(cells)))}
        row["detail_id"] = None
        for a in tr.find_all("a", href=_DETAIL_ID_RE):
            m = _DETAIL_ID_RE.search(a["href"])
            if m:
                row["detail_id"] = m.group(1)
                break
        rows.append(row)

    has_next = False
    pager = soup.find(class_=_PAGER_RE)
    if pager and pager.find("a", string=_NEXT_RE):
        has_next = True
    return rows, has_next


def next_page_url(html):
    soup  = BeautifulSoup(html, "lxml")
    pager = soup.find(class_=_PAGER_RE)
    if not pager:
        return None
    link = pager.find("a", string=_NEXT_RE)
    if link and link.get("href"):
        href = link["href"]
        return href if href.startswith("http") else BASE_URL + href
    return None


def fetch_detail(session, detail_id):
    """Fetch one Active pharmacy's detail page.

    Must run in the same session as the search that returned the ID.
    Inactive/Erased records return an error page — an empty dict is returned.
    """
    try:
        resp = session.get(f"{DETAIL_URL}/{detail_id}", timeout=15)
    except requests.RequestException:
        return {}
    if resp.status_code != 200 or "An error occurred" in resp.text:
        return {}
    soup   = BeautifulSoup(resp.text, "lxml")
    record = {}
    for tr in soup.find_all("tr"):
        th = tr.find("th")
        td = tr.find("td")
        if not th or not td:
            continue
        label = th.get_text(strip=True).lower()
        value = td.get_text(separator=" ", strip=True)
        col   = DETAIL_FIELD_MAP.get(label, re.sub(r"\s+", "_", label))
        if col not in record:
            record[col] = value
    return record


def fetch_details_parallel(session, detail_ids, workers=10):
    """Fetch detail pages concurrently; returns {detail_id: record}."""
    results = {}
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = {ex.submit(fetch_detail, session, d): d for d in detail_ids}
        for fut in as_completed(futures):
            results[futures[fut]] = fut.result()
    return results
