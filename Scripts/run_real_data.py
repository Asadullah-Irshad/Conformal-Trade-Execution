"""Run the real-data validation (paper Section 6): Figs 11-12 and Table 2.

Requires network access and yfinance. Free intraday history is limited, so this
is an indicative re-run of the pipeline on current data, not a bit-for-bit
reproduction of the published Table 2 / Figs 11-12 (those are archived in
Figures/ and Tables/).

Examples:
  python Scripts/run_real_data.py
  python Scripts/run_real_data.py --tickers AAPL MSFT AMZN --days 55
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "Src"))

from uae.real_data import run_real_data  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tickers", nargs="+", default=None,
                    help="ticker symbols (default: 30 US large-caps)")
    ap.add_argument("--days", type=int, default=55, help="days of 5-minute history to pull")
    args = ap.parse_args()
    run_real_data(tickers=args.tickers, days=args.days,
                  out_results=REPO / "Results", out_figures=REPO / "Figures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
