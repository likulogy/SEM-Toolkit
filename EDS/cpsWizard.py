import hyperspy.api as hs
import numpy as np

class cpsWizard:
    def averageCPS(spectrum):
        '''
        this method will returns average CPS(Count Per Second) during EDS analysis
        @spectrum : directory of spectrum
        '''
        loadedSpectrum = hs.load(spectrum)
        measure_time = loadedSpectrum.original_metadata.spc_header.liveTime
        total_dataPoints = loadedSpectrum.original_metadata.spc_header.numPts
        iteration = np.arange(0, (total_dataPoints - 1))

        total_xrayCount = 0
        for i in iteration:
            total_xrayCount = total_xrayCount + loadedSpectrum.data[i]
        cps_val = total_xrayCount / measure_time
        print(cps_val, total_xrayCount, measure_time)
        return cps_val

    def rangeCPS(spectrum, min, max):
        '''
        this method will returns average CPS of selected region
        @min : lower boundary of energy level
        @max : upper boundary of energy level
        @spectrum : directory of spectrum
        '''
        s = hs.load(spectrum)
        iteration = np.arange(min, max)
        measure_time = s.original_metadata.spc_header.liveTime
        total_xrayCount = 0
        for i in iteration:
            total_xrayCount = total_xrayCount + s.data[i]
            print(s.data[i])
        cps_inRegion = total_xrayCount / measure_time
        return cps_inRegion
    
    def totalCount(spectrum):
        '''
        this method will return sum of all recorded x-ray photon count.
        @spectrum : directory of spectrum
        '''
        s = hs.load(spectrum)
        
        total_dataPoints = s.original_metadata.spc_header.numPts
        iteration = np.arange(0, (total_dataPoints - 1))

        total_xrayCount = 0
        for i in iteration:
            total_xrayCount = total_xrayCount + s.data[i]
        return total_xrayCount
