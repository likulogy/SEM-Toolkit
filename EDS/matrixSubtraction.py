import hyperspy.api as hs


class removeMatrix:
	def __init__(self, directory):
		try:
			self.loadedSpectrum = hs.load(directory)
			self.directory = directory
		except:
			print('SPECTRUM LOADING FAILED')

	def setMatrixSpectrum(self, directory):
		try:
			self.matrixSpectrum = hs.load(directory)
			self.matrixDirectory = directory
		except:
			print('MATRIX LOAD FAILED')

	def setStandardLine(self, element, line):
		'''
		this function set a range of region by material database offered by HyperSpy that will be peak value analyzed.
		:param element: case sensitive, name of element
		:param line: case sensitive, name of x-ray line
		:return:
		'''
		lineEnergy = hs.material.elements[element]['Atomic_properties']['Xray_lines'][line][
			             'energy (keV)'] * 1000  # keV to eV

		tolerance = self.step * 10
		length_of_number = len(str(self.step))

		upperBoundary = round(lineEnergy + tolerance, -1 * length_of_number)
		lowerBoundary = round(lineEnergy - tolerance, -1 * length_of_number)

		self.rangeMinimum = lowerBoundary
		self.rangeMaximum = upperBoundary

	def setStandardRange(self, min, max):
		'''
		set a range of region by manual that peak value will be analyzed.
		:param min:
		:param max:
		:return:
		'''
		self.rangeMinimum = min
		self.rangeMaximum = max

	def getStandardRange(self):
		'''
		return lower and upper boundary of interested range.
		:return:
		'''
		return self.rangeMinimum, self.rangeMaximum

	def setEnergyStep(self, energyInterval):
		'''
		set energy interval manually.
		:param energyInterval:
		:return:
		'''
		self.step = energyInterval

	def getEnergyStep(self):
		'''
		return value of energy interval.
		:return:
		'''
		return self.step

	def setMatrixPeak(self):
		'''
		get maximum value of matrix spectrum in given range.
		:return:
		'''
		list = []
		stepMin = int(self.rangeMinimum / self.step)
		stepMax = int((self.rangeMaximum / self.step) + 1)
		for i in range(stepMin, stepMax):
			data = self.matrixSpectrum.data[i]
			list.append(data)
		self.matrixMaximumPeakValue = max(list)

	def setSpetrumPeak(self):
		'''
		get maximum value of spectrum in given range.
		:return:
		'''
		list = []
		stepMin = int(self.rangeMinimum / self.step)
		stepMax = int((self.rangeMaximum / self.step) + 1)
		for i in range(stepMin, stepMax):
			data = self.loadedSpectrum.data[i]
			list.append(data)
		self.spectrumMaximumPeakValue = max(list)

	def setCalibrationFactor(self):
		'''
		calculate calibration factor using maximum value of each spectrum in specific range(around specific peaks, ie Fe La or Ka)
		:return:
		'''
		self.calibrationFactor = self.spectrumMaximumPeakValue / self.matrixMaximumPeakValue

	def matrixSubtraction(self):
		'''
		perform matrix subtraction.
		:return:
		'''
		# Update matrix spectrum data with simple multiplication with calibration factor.
		iteration = len(self.matrixSpectrum.data)
		for i in range(iteration):
			self.matrixSpectrum.data[i] = self.matrixSpectrum.data[i] * self.calibrationFactor

		# perform subtraction using matrix spectrum.
		calibrationIteration = len(self.loadedSpectrum.data)
		for i in range(calibrationIteration):
			update = int(self.loadedSpectrum.data[i]) - int(self.matrixSpectrum.data[i])
			self.loadedSpectrum.data[i] = update

	def export(self):
		'''
		return matrix-subtracted spectrum as list.
		while x-ray count value only exported, energy level corresponding each x-ray intensity must be reconstructed using known step interval.
		:return:
		'''
		DataExport = []
		iteration = len(self.matrixDirectory)
		for i in iteration:
			DataExport.append(self.loadedSpectrum.data[i])
		return DataExport


if __name__ == '__main__':
	# initialize class
	calibration = removeMatrix('/Users/LIKU/Desktop/code/SEM-Toolkit/EDS/sample/precipitates.spc')
	calibration.loadedSpectrum.plot()

	# load spectrum file of matrix
	calibration.setMatrixSpectrum('/Users/LIKU/Desktop/code/SEM-Toolkit/EDS/sample/matrix.spc')
	# set energy interval of loaded spectrum. this value will be applied both of loaded spectra.
	calibration.setEnergyStep(10)

	# set standard X-ray line for calibrate. in this case Fe Ka selected to perform calibration based on intensity of Fe Ka line.
	calibration.setStandardLine('Fe', 'Ka')
	# calibration.setStandardRange(600, 800) #this also possible to manually set range.

	# valdate calibration range. output value must contain Fe La X-ray line, 700eV
	print(calibration.getStandardRange())

	# find maximum value of peak between range around 700eV.
	calibration.setMatrixPeak()
	calibration.setSpetrumPeak()

	# calculate calibration factor for match Fe La peak.
	calibration.setCalibrationFactor()

	# perform matrix subtraction
	calibration.matrixSubtraction()

	# plot calibrated spectrum.
	calibration.loadedSpectrum.plot()

	# load original precipitate spectrum and matrix for comparison.
	original = hs.load('/Users/LIKU/Desktop/code/SEM-Toolkit/EDS/sample/precipitates.spc')
	matrix = hs.load('/Users/LIKU/Desktop/code/SEM-Toolkit/EDS/sample/matrix.spc')

	# plot both unmodified spectrum.
	original.plot()
	matrix.plot()