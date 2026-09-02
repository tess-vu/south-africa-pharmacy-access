import yaml
from .paths import REPO_ROOT

CONFIG_PATH = REPO_ROOT / "config" / "analysis.yml"


def load_config():
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)
