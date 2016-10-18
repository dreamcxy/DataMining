import numpy as np

oldDataTrainMatrix = []
dataTrainDegree = []
with open('dataset2_training.txt', 'r') as dataFile:
    data = dataFile.readlines()
    for line in data:
        numbers = map(float, line.split(','))
        oldDataTrainMatrix.append(numbers[:-1])
        dataTrainDegree.append(numbers[-1])
oldDataTrainMatrix = np.array(oldDataTrainMatrix)
dataTrainDegree = np.array(dataTrainDegree)

u, sigma, vt = np.linalg.svd(oldDataTrainMatrix.T)
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
lowTrainMat = np.dot(kTrainVectors, oldDataTrainMatrix.T)

oldTestDataMatrix = []
oldTestDegree = []
with open('dataset2_testing.txt', 'r') as testDataFile:
    testData = testDataFile.readlines()
    for testLine in testData:
        testNumbers = map(float, testLine.split(','))
        oldTestDataMatrix.append(testNumbers[:-1])
        oldTestDegree.append(testNumbers[-1])
oldTestDataMatrix = np.array(oldTestDataMatrix)
oldTestDegree = np.array(oldTestDegree)
uTest, sigTest, vtTest = np.linalg.svd(oldTestDataMatrix.T)
uKMax = []
for i in range(0, uTest.shape[0]):
    uKMax.append(np.linalg.norm(uTest[i]))
uKMax = np.array(uKMax)
uKMaxPosition = np.argsort(-uKMax)
kTestValues = uKMaxPosition[:k]
kTestVectors = []
for position in kTestValues:
    kTestVectors.append(uTest[position])
kTestVectors = np.array(kTestVectors)
print uKMax.shape
print kTestVectors.shape
print oldTestDataMatrix.shape

lowTestMat = np.dot(kTrainVectors, oldTestDataMatrix.T)

correct = 0
for testVector in lowTestMat.T:
    position = 0
    minDistance = []
    for trainVector in lowTrainMat.T:
        minDistance.append(np.linalg.norm(testVector - trainVector))
    minDistance = np.array(minDistance)
    minPosition = minDistance.argmin()
    newTestDegree = dataTrainDegree[minPosition]
    if newTestDegree == oldTestDegree[position]:
        correct += 1
    position += 1
print correct
print float(lowTestMat.shape[1])
print correct / float(lowTestMat.shape[1])
