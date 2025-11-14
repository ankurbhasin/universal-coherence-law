#!/usr/bin/env python3
"""
Stub only.

ibmq_build_integration_windows.py

Role:
  - Load IBM Q single qubit experiment CSV files, such as:
      ibm_fez_Ramsey_q0.csv
      ibm_fez_T1_q1.csv
      ibm_marrakesh_CPMG4_q3.csv
      ibm_torino_Hahn_q0.csv
  - Interpret the time and response columns.
  - For each time series:
      * apply a suitable window
      * compute power spectral density
      * integrate power in fixed bands:
          delta, theta, alpha, beta, gamma
      * normalise to obtain relative band powers
      * define an information variable I_entropy
  - Aggregate into:
      data/quantum/ibmq_integration_windows.csv
      and mirror into:
      runs/quantum_scaling/ibmq_phase01/phase30/integration_windows.csv

The full numerical logic (choices of dt, band edges, windowing, and
entropy measure) is part of the private reproducibility package and
is not released here.
"""

if __name__ == "__main__":
    raise RuntimeError(
        "Stub only. IBM Q integration window builder is not included "
        "in this public repository."
    )
