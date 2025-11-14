#!/usr/bin/env python3
"""
Stub only.

helio_preprocess.py

Role:
  - Load BiSON Sun-as-a-star velocity time series from:
      allsites-waverage-quality.fits
    or similar FITS products.
  - Extract the main time series.
  - Remove long term trends and the mean.
  - Apply a bandpass filter that isolates the p-mode range
    (for example 0.5 to 8.0 mHz, expressed in Hz).
  - Save a cleaned CSV:
      data/helio/clean_helio.csv
    with columns such as:
      t_sec, v_clean

This provides the input series for the sliding window integration used
in helio_build_integration_windows.py.

Full numeric implementation is withheld until after peer review.
"""

if __name__ == "__main__":
    raise RuntimeError(
        "Stub only. Helioseismic preprocessing code is not released yet."
    )
