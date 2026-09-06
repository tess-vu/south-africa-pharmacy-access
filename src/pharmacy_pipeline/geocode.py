import os
import time
import pandas as pd
import requests

TEXTSEARCH_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"

# Google Places returns lat/lng in EPSG:4326 (latitude first in the response body)
_EMPTY = {
    "place_id": None,
    "matched_name": None,
    "matched_address": None,
    "lat": None,
    "lng": None,
    "types": None,
    "raw_error": None,
}

RETRYABLE_STATUSES = {"OVER_QUERY_LIMIT", "UNKNOWN_ERROR"}


def get_api_key():
    key = os.getenv("GOOGLE_MAPS_API_KEY")
    if not key:
        raise RuntimeError("GOOGLE_MAPS_API_KEY not set — see .env.example")
    return key


def build_query(row, fields):
    """Join non-empty row values for the given fields, always ending with 'South Africa'."""
    parts = []
    for f in fields:
        v = row.get(f)
        if pd.isna(v):
            continue
        v = str(v).strip()
        if v and v != "nan":
            parts.append(v)
    parts.append("South Africa")
    return ", ".join(parts)


def places_text_search(query, api_key, place_type="pharmacy",
                       retries=3, backoff=2.0, timeout=30):
    """Places (legacy) Text Search returning the first result.

    Returns dict with keys: http_status, api_status, place_id, matched_name,
    matched_address, lat, lng, types, raw_error. Retries network failures and
    OVER_QUERY_LIMIT with exponential backoff.
    """
    params = {"query": query, "type": place_type, "key": api_key}
    last_error = None

    for attempt in range(retries + 1):
        if attempt:
            time.sleep(backoff * 2 ** (attempt - 1))
        try:
            r = requests.get(TEXTSEARCH_URL, params=params, timeout=timeout)
        except requests.RequestException as e:
            last_error = str(e)
            continue

        try:
            data = r.json()
        except ValueError:
            return {"http_status": r.status_code, "api_status": "BAD_JSON",
                    **_EMPTY, "raw_error": r.text[:500]}

        status = data.get("status")
        if status in RETRYABLE_STATUSES:
            last_error = str(data)[:500]
            continue
        if status != "OK":
            return {"http_status": r.status_code, "api_status": status,
                    **_EMPTY, "raw_error": str(data)[:500]}

        result = data["results"][0]
        loc = result.get("geometry", {}).get("location", {})
        return {
            "http_status": r.status_code,
            "api_status": status,
            "place_id": result.get("place_id"),
            "matched_name": result.get("name"),
            "matched_address": result.get("formatted_address"),
            "lat": loc.get("lat"),
            "lng": loc.get("lng"),
            "types": ", ".join(result.get("types", [])) or None,
            "raw_error": None,
        }

    return {"http_status": None, "api_status": "REQUEST_FAILED",
            **_EMPTY, "raw_error": last_error}


def needs_review(row):
    if row["api_status"] != "OK":
        return True
    if pd.isna(row["place_id"]):
        return True
    if pd.isna(row["lat"]) or pd.isna(row["lng"]):
        return True
    return False
