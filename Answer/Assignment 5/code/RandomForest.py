import math
from numpy import *

def loadDataSet(fileName, fileNum):
    dataSet = []
    fr = open(fileName)
    for line in fr:
        line = line.split(',')
        data = [float(i) for i in line]
        if data[-1] == 0:
            data[-1] = -1
        dataSet.append(data)
    fr.close()
    if fileNum == 0:
        for i in range(3):
            dataSet.append(dataSet[random.randint(1, 278)])
    dataSet = array(dataSet[1:])
    if fileNum == 1:
        for j in range(12):
            if len(set(dataSet[:, j])) > 4:
                minRange = min(dataSet[:, j])
                maxRange = max(dataSet[:, j]) + 0.01
                rangeX = linspace(minRange, maxRange, 5)
                for i in range(dataSet.shape[0]):
                    for k in range(4):
                        if rangeX[k] <= dataSet[i,j] < rangeX[k+1]:
                            dataSet[i, j] = k
    return dataSet

def entropy(dataSet):
    labels = dataSet[:, -1]
    prob1 = len(labels[labels == -1]) / dataSet.shape[0]
    prob2 = 1 - prob1
    if prob1 < 1e-5 or prob2 < 1e-5:
        return 0
    entropy = -prob1 * math.log(prob1, 2) - prob2 * math.log(prob2, 2)
    return entropy

def dataSetProcess(dataSet, axis, value):
    retDataSet = []
    for i in range(dataSet.shape[0]):
        if dataSet[i, axis] == value:
            data = list(dataSet[i, :])
            retDataSet.append(data)
    return array(retDataSet)

def bestFeature(dataSet, featuresRange):
    numberFeatures = len(featuresRange)
    baseEntropy = entropy(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numberFeatures):
        uniqueVals = set(dataSet[:, featuresRange[i]])
        newEnt = 0.0
        for value in uniqueVals:
            dataSetSub = dataSetProcess(dataSet, featuresRange[i], value)
            prob = len(dataSetSub) / len(dataSet)
            newEnt += prob * entropy(dataSetSub)
        infoGain = baseEntropy - newEnt
        if infoGain >= bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = featuresRange[i]
    return bestFeature, bestInfoGain

def vote(labelList):
    x = len(labelList[labelList == -1])
    y = len(labelList[labelList == 1])
    if x >= y:
        return -1
    else:
        return 1

def decisionTree(dataSet):
    labelList = dataSet[:, -1]
    if len(set(labelList)) == 1:
        return labelList[0]
    n = dataSet.shape[1]
    featNum = int(math.sqrt(n-1))
    featuresRange = []
    while True:
        x = random.randint(n-1)
        if x not in featuresRange:
            featuresRange.append(x)
        if len(featuresRange) == featNum:
            break
    bestFeat, bestInfoGain = bestFeature(dataSet, featuresRange)
    if bestInfoGain == 0:
        return vote(labelList)
    if len(set(dataSet[:, bestFeat])) == 1:
        return vote(labelList)
    tree = {bestFeat:{}}
    uniqueVals = set(dataSet[:, bestFeat])
    for value in uniqueVals:
        dataSetSub = dataSetProcess(dataSet, bestFeat, value)
        tree[bestFeat][value] = decisionTree(dataSetSub)
    return tree

def decisiondecisionTreeClassify(decisionTreeInput, testVector):
    if type(decisionTreeInput).__name__ == 'int':
        return decisionTreeInput
    featuresIndex = list(decisionTreeInput.keys())[0]
    branchDict = decisionTreeInput[featuresIndex]
    classLabel = 0
    for branch in branchDict:
        if testVector[featuresIndex] == branch:
            if type(branchDict[branch]).__name__ == 'dict':
                classLabel = decisiondecisionTreeClassify(branchDict[branch], testVector)
            else:
                classLabel = branchDict[branch]
    return classLabel

def sample(dataSet):
    m = dataSet.shape[0]
    indices = list(random.randint(m, size = m))
    return dataSet[indices, :]

def randomForestTraining(trainDataSet):
    treeNum = 1000
    weakClassifier = []
    for i in range(treeNum):
        dataSet = sample(trainDataSet)
        tree = decisionTree(dataSet)
        weakClassifier.append(tree)
    return weakClassifier

def randomForestClassify(testDataSet, weakClassifier):
    m = testDataSet.shape[0]
    aggClassEst = array([0] * m)
    labels = testDataSet[:, -1]
    for i in range(len(weakClassifier)):
        classEst = array([0] * m)
        for j in range(m):
            classEst[j] = decisiondecisionTreeClassify(weakClassifier[i], testDataSet[j])
        aggClassEst += classEst
    errorRate = 0
    for j in range(m):
        if labels[j] * aggClassEst[j] < 0:
            errorRate += 1
        if aggClassEst[j] == 0:
            if labels[j] == -1:
                errorRate += 1
    errorRate /= m
    return errorRate

def _10foldCrossValidation(dataSet):
    correctRate = []
    step = dataSet.shape[0] / 10
    allSet = set(arange(dataSet.shape[0]))
    for fold in range(10):
        testSet = set(arange(fold * step, (fold + 1) * step))
        trainSet = allSet - testSet
        testDataSet = dataSet[list(testSet), :]
        trainDataSet = dataSet[list(trainSet), :]
        weakClassifier = randomForestTraining(trainDataSet)
        correctRate.append(1 - randomForestClassify(testDataSet, weakClassifier))
    return array(correctRate)

print("Random Forest Algorithm")
fileName = ["breast-cancer-assignment5.txt", "german-assignment5.txt"]
for i in range(len(fileName)):
	print("Processing the dataSet ", i + 1)
	dataSet = loadDataSet(fileName[i], i)
	correctRate = _10foldCrossValidation(dataSet)
	print("The correct rate on dataSet " ,i + 1, "is: \n", correctRate)
	meanCorrect = mean(correctRate)
	stdCorrect = std(correctRate)
	print("The average on dataSet ", i + 1, "is: ", meanCorrect, "standard deviation on dataSet ", i + 1, "is: ", stdCorrect)























