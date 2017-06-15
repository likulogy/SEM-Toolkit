import hyperspy.api as hs

class peakWizard:
    def possibleElements(spectrum):
        '''
        this method will returns list of all possible elements of given spectrum.
        @spectrum : directory of spectrum
        '''
        s = hs.load(spectrum)
        peaks = s.find_peaks1D_ohaver(maxpeakn=1)[0]
        possible = hs.eds.get_xray_lines_near_energy(peaks['position'])
        return possible

    def possiblePeak(spectrum):
        '''
        this method will returns list of possible peak by peak detection method
        @spectrum : directory of spectrum
        '''
        s = hs.load(spectrum)
        peaks = s.find_peaks1D_ohaver(maxpeakn=1)[0]
        return peaks
