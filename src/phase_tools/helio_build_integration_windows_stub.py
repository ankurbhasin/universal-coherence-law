#!/usr/bin/env python3
"""
Stub only.

helio_build_integration_windows.py

Role:
  - Take the cleaned Sun-as-a-star time series (for example clean_helio.csv).
  - Define sliding windows in time, with chosen length and hop size.
  - For each window:
      * compute the power spectral density
      * integrate power in the same band definitions used elsewhere
        (delta, theta, alpha, beta, gamma, in solar p-mode range)
      * compute an information or entropy like measure for that window
        (I_entropy)
  - Output:
      runs/helio_scaling/phase30/integration_windows.csv

These integration windows feed directly into vuh_scaling_law.py to
extract the helioseismic contribution to the universal beta law.

This is a non executable stub. The actual implementation is stored in
a private archive for peer review.
"""

if __name__ == "__main__":
    raise RuntimeError(
        "Stub only. Helio integration window code will be released after publication."
    )
