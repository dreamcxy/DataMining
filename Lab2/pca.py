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
# print oldDataTrainMatrix.shape
# print dataDegree


def dealOldMatrix(oldDataMatrix):
    meanVal = np.mean(oldDataMatrix, axis=0)
    newData = oldDataMatrix - meanVal
    return newData, meanVal

newDataTrainMatrix, meanTrainValue = dealOldMatrix(oldDataTrainMatrix)
covTrainMatrix = np.cov(newDataTrainMatrix, rowvar=0)

eigTrainValues, eigTrainVectors = np.linalg.eig(np.mat(covTrainMatrix))

k = 20
kTrainEigValues = np.argsort(eigTrainValues)[-1:-(k + 1):-1]
kTrainEigVectors = eigTrainVectors[:, kTrainEigValues]
lowTrainDegreeDatMat = newDataTrainMatrix * kTrainEigVectors
# reconTrainMat = (lowTrainDegreeDatMat * kTrainEigVectors.T) + meanTrainValue
# print reconTrainMat

print kTrainEigVectors.shape

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
newDataTestMatrix, meanTestValue = dealOldMatrix(oldTestDataMatrix)
covTestMatrix = np.cov(newDataTestMatrix, rowvar=0)
eigTestValues, eigTestVectors = np.linalg.eig(np.mat(covTestMatrix))
kTestEigValues = np.argsort(eigTestValues)[-1:-(k + 1):-1]
kTestEigVectors = eigTestVectors[:, kTestEigValues]
lowTestDegreeDatMat = np.dot(newDataTestMatrix, kTestEigVectors)

correct = 0
for testVector in lowTestDegreeDatMat:
    position = 0
    minDistance = []
    for trainVector in lowTrainDegreeDatMat:
        minDistance.append(np.linalg.norm(testVector - trainVector))
    minDistance = np.array(minDistance)
    minPosition = minDistance.argmin()
    newTestDegree = dataTrainDegree[minPosition]
    if newTestDegree == oldTestDegree[position]:
        correct = correct + 1
    position = position + 1
print correct / float(lowTestDegreeDatMat.shape[0])
