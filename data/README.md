# Data

No datasets are committed to this repository. This file documents every input,
where it comes from, and how to reproduce the intermediates.

Working CRS: EPSG:32735 (UTM 35S) for all distance/area computation.
Source coordinates: EPSG:4326 (lon/lat).

## Directory Layout

```
data/
├── reference/ # small lookup tables
│ ├── CITY_PROVINCE_LOOKUP.csv
│ ├── sa_geographic_lookup.csv
│ └── Wards_2023.csv
├── raw/ # downloaded sources (gitignored)
│ ├── 2011_census/
│ ├── 2023_census/
│ ├── sal_w_ward_new/
│ └── pharmacy_sources/ # insurer lists, SAPC scrape output
├── interim/ # pipeline intermediates (gitignored)
└── processed/ # final outputs (gitignored)
```

## Sources

| Dataset | Source | Access | License / Terms |
|---|---|---|---|
| 2011 Census SAL/EA boundaries + demographics | Stats SA (superweb.statssa.gov.za) | Download SAL-level shapefiles for GP + KZN | Stats SA terms, not redistributable here |
| 2023 ward boundaries (`SA_Wards2020.shp`) + `wards_pop.csv` | Municipal Demarcation Board / Stats SA | Direct download | Public |
| Census 2022 (`SA_CENSUS_2022_{GEOGRAPHY,HOUSEHOLD,PERSON}.csv`) | Stats SA | Direct download | Stats SA terms |
| `sal_w_ward_new.shp` | Team-produced (ArcGIS spatial join, teammate Jill) | Request from project Box/Drive | Internal |
| Insurer pharmacy lists (GEMS, Momentum, Wooltru, SAMWUMED, Vitality) | Provided by DAIR, loaded to BigQuery RAW | Request from DAIR | Publicly available from pharmacy websites |
| Hospital list (`RAW.PHARMACIES_HOSPITALS`) | DAIR, pre-cleaned | Request from DAIR | Internal |
| SAPC pharmacy register | Scraped from pharmcouncil.co.za (NB `01_sapc_scraper_1.ipynb`) | Re-run scraper | Public registry |
| Geocoding results | Google Places API (NBs 02, 04) | Re-run with `GOOGLE_MAPS_API_KEY`, billed | Google Maps Platform ToS |
| Road networks (4 GraphML files) | OpenStreetMap via OSMnx 2.1.0 (NB 3) | Re-run NB 3 (26–88 min per graph) | ODbL |
| Fonts (Space Grotesk, Space Mono) | fonts.google.com | Install locally | OFL |

## Reproducing Intermediates

Run Pipeline A (SQL 01–05 in BigQuery, then notebooks 01–05 in `notebooks/pharmacy_gathering/clean process/`) to produce `PHARMACIES_MASTER_FINAL.csv`, then Pipeline B notebooks 1–8 in order (see pipeline_documentation.md for contracts and runtimes).

Long-running steps, do not re-run casually:
- NB 3 network download
- NB 6 k=3 Dijkstra distances

Disk Requirement: ~3 GB for all raw + intermediate data.
