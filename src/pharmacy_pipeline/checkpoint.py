from pathlib import Path
import pandas as pd


def load_checkpoint(path, key):
    """Return (existing_df, done_keys) from a checkpoint CSV, or (empty df, empty set)."""
    p = Path(path)
    if p.exists():
        df = pd.read_csv(p, dtype=str)
        return df, set(df[key].dropna())
    return pd.DataFrame(), set()


def save_checkpoint(existing, new_rows, path, key):
    """Append new_rows to existing, dedup on key (first wins), write CSV. Returns the combined frame."""
    combined = pd.concat([existing, pd.DataFrame(new_rows)], ignore_index=True)
    combined = combined.drop_duplicates(subset=[key], keep="first")
    combined.to_csv(path, index=False)
    return combined
