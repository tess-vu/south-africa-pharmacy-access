from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# notebooks/data is the live pipeline contract location; a future move to
# a root-level data/ tree only requires changing this one line.
DATA = REPO_ROOT / "notebooks" / "data"

NETWORKS = DATA / "networks"
COMBINED = DATA / "combined"
FIGURES = REPO_ROOT / "notebooks" / "figures"

SAL_W_WARD_NEW   = DATA / "sal_w_ward_new" / "sal_w_ward_new.shp"
SAL_W_WARD_DEDUP = DATA / "sal_w_ward_dedup" / "sal_w_ward_dedup.shp"
CENSUS_2011_SAL  = DATA / "2011_census" / "2011_Census" / "ea_sal_kzn_gp.shp"
WARDS_2020_SHP   = DATA / "2023_census" / "2023_census" / "SA_Wards2020.shp"
WARDS_POP_CSV    = DATA / "2023_census" / "wards_pop.csv"
POP_PRED_FINAL   = DATA / "pop_pred_final.csv"
PHARMACIES_MASTER = DATA / "PHARMACIES_MASTER_FINAL.csv"
TESS_ALL_ACCESS        = DATA / "tess_all_access.csv"
TESS_ALL_ACCESS_W_SNAP = DATA / "tess_all_access_w_snap.csv"
SAL_PHARM_DIST_K3   = NETWORKS / "sal_pharmacy_distances_k3.csv"
SAL_PHARM_DIST_K1   = NETWORKS / "sal_pharmacy_distances.csv"
THRESHOLD_FLAGS_K3  = NETWORKS / "sal_threshold_flags_k3.csv"
THRESHOLD_SUMMARY_K3 = NETWORKS / "threshold_summary_k3.csv"
SAL_COMBINED_CSV    = COMBINED / "sal_combined_access.csv"
SAL_COMBINED_SHP    = COMBINED / "sal_combined_access_shp" / "sal_combined_access.shp"