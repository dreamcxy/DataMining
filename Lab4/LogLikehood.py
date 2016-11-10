from numpy import*


def loadData(FileName):
	dataMatrix = []
	dataLabel = []
	with open(FileName, 'r') as dataFile:
		dataLines = dataFile.readlines()
		for line in dataLines:
			data = map(float, line.split(','))
			dataMatrix.append(data[:-1])
			dataLabel.append(data[-1])
	return dataMatrix, dataLabel


def


def main():
	dataMatrix, dataLabel = loadData('test.txt')
	print dataLabel






main()