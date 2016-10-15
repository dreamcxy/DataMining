import numpy as np

oldDataTrainMatrix = []
dataTrainDegree = []
with open('dataset1_training.txt', 'r') as dataFile:
    data = dataFile.readlines()
    for line in data:
        numbers = map(float, line.split(','))
        oldDataTrainMatrix.append(numbers[:-1])
        dataTrainDegree.append(numbers[-1])
oldDataTrainMatrix = np.array(oldDataTrainMatrix)
dataTrainDegree = np.array(dataTrainDegree)
oldTestDataMatrix = []
oldTestDegree = []
with open('dataset1_testing.txt', 'r') as testDataFile:
    testData = testDataFile.readlines()
    for testLine in testData:
        testNumbers = map(float, testLine.split(','))
        oldTestDataMatrix.append(testNumbers[:-1])
        oldTestDegree.append(testNumbers[-1])
oldTestDataMatrix = np.array(oldTestDataMatrix)
oldTestDegree = np.array(oldTestDegree)

print oldDataTrainMatrix.shape
u, sig, v = np.linalg.svd(oldDataTrainMatrix)
uKMax = []
k = 10
for i in range(0, u.shape[0]):
    uKMax.append(np.linalg.norm(u[i]))
uKMax = np.array(uKMax)
uKMaxPosition = np.argsort(-uKMax)
kTrainValues = uKMaxPosition[:k]
kTrainVectors = []
for position in kTrainValues:
    kTrainVectors.append(u[position])
kTrainVectors = np.array(kTrainVectors)

print kTrainVectors.shape
