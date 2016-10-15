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

u, sigma, vt = np.linalg.svd(oldDataTrainMatrix)
uKMax = []
k = 30
for i in range(0, u.shape[0]):
    uKMax.append(np.linalg.norm(u[i]))
uKMax = np.array(uKMax)
uKMaxPosition = np.argsort(-uKMax)
kTrainValues = uKMaxPosition[:k]
kTrainVectors = []
for position in kTrainValues:
    kTrainVectors.append(u[position])
kTrainVectors = np.array(kTrainVectors)
lowTrainMat = np.dot(kTrainVectors, oldDataTrainMatrix)

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
uTest, sigTest, vtTest = np.linalg.svd(oldTestDataMatrix)
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
print kTestVectors.shape
print oldTestDataMatrix.shape
lowTestMat = np.dot(kTestVectors, oldTestDataMatrix)

correct = 0
for testVector in lowTestMat:
    position = 0
    minDistance = []
    for trainVector in lowTrainMat:
        minDistance.append(np.linalg.norm(testVector - trainVector))
    minDistance = np.array(minDistance)
    minPosition = minDistance.argmax()
    newTestDegree = dataTrainDegree[minPosition]
    if newTestDegree == oldTestDegree[position]:
        correct = correct + 1
    position = position + 1

print correct / 103.0
