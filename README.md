# universal-coherence-law
A Universal Coherence Law: Frequency–Information Scaling

This directory documents the expected data layout used by the full
Universal Coherence Law analysis pipeline. No real data are included.

Typical top level layout used in the private archive:

- `data/eeg/`  
  EEG open data (for example PhysioNet eegmmidb).

- `data/gw/`  
  LIGO strain time series for selected binary black hole events.

- `data/materials/`  
  Phonon spectra harvested from open materials databases.

- `data/quantum/`  
  - `ibmq_integration_windows.csv` built from IBM Q device runs.

- `data/helio/`  
  - `allsites-waverage-quality.fits` (BiSON download).
  - `clean_helio.csv` after preprocessing.

- `runs/`  
  Per domain run folders with phase specific outputs.

All of the above are kept outside this public repository and will be
released later through a dedicated data archive.
