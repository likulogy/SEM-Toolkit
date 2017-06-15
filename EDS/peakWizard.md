# Purpose of this Code
This code snippet is simple wrapper of HyperSpy. with this code, possible element in specific peak can be automatically analyzed, or peak detection possible.

But, all functionalities of this code are easily achieved with pure HyperSpy library.

# Functionality
- list of all possible peaks in given spectrum with `possiblePeak(spectrum)`
- list of all possible elements in given spectrum with `possibleElements(spectrum)`

## Usage(Examples)
- rough evaluation of possible elements in EDS spectra.
- fast insight to proper elements to put together in Model or x-ray line.
```python
import peakWizard

directory = 'spectrum.spc'
peakWizard.averageCPS(directory)
```

# Dependencies
- Python 3+
- HyperSpy