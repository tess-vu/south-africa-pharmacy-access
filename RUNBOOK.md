# Runbook for south-africa-pharmacy-access

End-to-end execution guide. What each stage needs, in what order, and how long
it takes. Contracts and schemas live in pipeline_documentation.md.

## Environment

    conda env create -f environment.yml
    conda activate sa-pharmacy-access
    copy .env.example .env    # fill in GOOGLE_MAPS_API_KEY etc.

Notebooks resolve paths through src/paths.py and run from any working
directory. Analysis constants live in config/analysis.yml.

Disk: ~2–3 GB (census shapefiles, 4 GraphML networks ~50 MB+ each,
intermediates). Data sources and download instructions: data/README.md.

## Pipeline A: Pharmacy File

BigQuery (datasets RAW, INTERMEDIATE), then notebooks in
notebooks/pharmacy_gathering/clean process/:

| Step | Runtime | Notes |
|---|---|---|
| sql/01–05 in order | minutes | 02 must run before re-running 03 steps 6–9 |
| 01_sapc_scraper_1.ipynb | 1–2 h | resumable from checkpoint |
| 02_google_places_extract.ipynb | ~1 h, billed API | checkpoint-resumable |
| 03_sapc_pharma_join.ipynb | minutes | |
| 04_sapc_geocode_unmatched_1.ipynb | minutes–1 h, billed API | |
| 05_final_master_pharma_1.ipynb | minutes + re-geocode pass | writes PHARMACIES_MASTER_FINAL.csv |

## Pipeline B: Accessibility Analysis (notebooks/, strict order)

| # | Notebook | Runtime | Output |
|---|---|---|---|
| 1 | sal_w_ward_deduplication.ipynb | minutes | sal_w_ward_dedup.shp |
| 2 | tess_newpred_compute.ipynb | minutes | pop_pred_final.csv |
| — | tess_newpred_visuals.ipynb | minutes | figures only |
| 3 | osmnx_network_download.ipynb | **26–88 min per graph** (skips existing) | 4 GraphML files |
| 4 | 2sfca_compute.ipynb | **hours** (graph loads + 4 Dijkstra sweeps) | tess_all_access.csv |
| — | 2sfca_visuals.ipynb | minutes | figures only |
| 5 | snap_distance_append.ipynb | 10–20 min (graph loads) | tess_all_access_w_snap.csv |
| 6 | sal_pharmacy_distance_k3.ipynb | **hours** (per-pharmacy Dijkstra, checkpointed every 50) | sal_pharmacy_distances_k3.csv |
| 7 | network_threshold.ipynb | minutes | sal_threshold_flags_k3.csv |
| 8 | combine_access_score_network_threshold.ipynb | minutes | sal_combined_access.csv + shapefile |

Do not casually re-run 3, 4, or 6. Both long Dijkstra notebooks resume from
checkpoints in data/networks/checkpoints/.

## Pipeline C: App Precompute

notebooks/mart_dataset_prep/ converts Pipeline B outputs to GeoJSON for
Mapbox. Note: shapefile/tileset field names are DBF-truncated to 10 chars
(walk_typology → walk_typol); ui_ux/README.md documents the frontend contract.

## Verification

- pop_pred_final.csv: 38,380 rows; sum(sal2023_est) equals ward 2023 total
- tess_all_access.csv: 38,380 rows with Ai_walk, Ai_drive, node
- sal_combined_access.csv: 38,380 rows; walk_typology/drive_typology contain
  exactly {Well-Served, Demand Overcrowding, Connectivity Gap, Access Gap,
  Pharmacy Desert, Artifact Zone}