from pathlib import Path


def ensure_dir(path):
    """mkdir -p equivalent; returns the path as a Path."""
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p
