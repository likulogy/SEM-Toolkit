# Purpose of this Code
This code written for evaluate CPS value of EDS Spectrum.

# Functionality
- CPS(Count Per Second) calculation with given EDS spectrum file.
- at this moment, SPC format only supported during use of SPC-only properties.
    - more spectra extensions will be supported near-future.
- simple average CPS value can be calculated with `averageCPS(spectrum_directory)`
- CPS value by specific range also possible with `rangeCPS(spectrum, min, max)`
- number of total recorded x-ray photon counts can be calculated with `totalCount(spectrum)`

## Usage(Examples)
- calculate possibilities of occurrence of sum-peak.
- calculate CPS value of specific areas.
```python
import cpsWizard

directory = 'spectrum.spc'
cpsWizard.averageCPS(directory)
```

# Dependencies
- Python 3+
- HyperSpy