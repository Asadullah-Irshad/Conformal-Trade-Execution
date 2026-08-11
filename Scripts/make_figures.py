"""Regenerate all simulator-based paper figures (Figs 1-10) into Figures/.

Every figure is produced from a fixed seed via the uae.figures module, so the
qualitative results in the paper are fully reproducible. The two real-data
figures (Figs 11-12) require downloading intraday data; see Scripts/run_real_data.py.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "Src"))

from uae.figures import make_all  # noqa: E402


def main() -> int:
    written = make_all(REPO / "Figures")
    print("Wrote", len(written), "figures to Figures/:")
    for name in written:
        print("  -", name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
