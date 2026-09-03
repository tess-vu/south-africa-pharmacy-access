import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
from .paths import DATA

FONT_TITLE = "Space Mono"     # titles, subtitles, legend titles
FONT_BODY  = "Space Grotesk"  # axis labels, tick labels, legend item labels

_MONO_FILES = [
    "Space_Mono/SpaceMono-Regular.ttf",
    "Space_Mono/SpaceMono-Bold.ttf",
    "Space_Mono/SpaceMono-Italic.ttf",
    "Space_Mono/SpaceMono-BoldItalic.ttf",
]
_GROTESK_FILES = [
    "Space_Grotesk/static/SpaceGrotesk-Regular.ttf",
    "Space_Grotesk/static/SpaceGrotesk-Medium.ttf",
    "Space_Grotesk/static/SpaceGrotesk-Bold.ttf",
    "Space_Grotesk/static/SpaceGrotesk-Light.ttf",
    "Space_Grotesk/static/SpaceGrotesk-SemiBold.ttf",
]


def setup_fonts():
    """Register the project fonts and set shared rcParams.

    Falls back to matplotlib defaults if the font files are absent
    (they are gitignored; see data/README.md).
    """
    missing = []
    for rel in _MONO_FILES + _GROTESK_FILES:
        p = DATA / rel
        if p.exists():
            fm.fontManager.addfont(str(p))
        else:
            missing.append(rel)

    available = {f.name for f in fm.fontManager.ttflist}
    ok = FONT_TITLE in available and FONT_BODY in available
    if not ok:
        print(f"Project fonts unavailable ({len(missing)} files missing) — using defaults")

    plt.rcParams.update({
        "font.family":           FONT_BODY if ok else "sans-serif",
        "axes.titlesize":        14,
        "axes.labelsize":        11,
        "xtick.labelsize":       10,
        "ytick.labelsize":       10,
        "legend.fontsize":       10,
        "legend.title_fontsize": 11,
    })
    return ok
