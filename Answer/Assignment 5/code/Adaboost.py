import math
from numpy import *

def dataProcess(fileName, fileNum):
    dataSet = []
    fr = open(fileName)
    for line in fr:
        line = line.split(',')
        data = [float(item) for item in line]
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
            if len(set(dataSet[:, j])) > 3:
                minRange = min(dataSet[:, j])
                maxRange = max(dataSet[:, j]) + 0.01
                rangeX = linspace(minRange, maxRange, 4)
                for i in range(dataSet.shape[0]):
                    for k in range(3):
                        if rangeX[k] <= dataSet[i,j] < rangeX[k+1]:
                            dataSet[i, j] = k
    return dataSet

def entropy(dataSet, weight):
    labels = dataSet[:, -1]
    prob1 = sum(weight[labels == -1]) / sum(weight)
    prob2 = sum(weight[labels == 1]) / sum(weight)
    if prob1 < 1e-5 or prob2 < 1e-5:
        return 0
    entropy = -prob1 * math.log(prob1, 2) - prob2 * math.log(prob2, 2)
    return entropy

def dataSetProcess(dataSet, axis, value, weight):
    retDataSet = []
    retWeight = []
    for i in range(dataSet.shape[0]):
        if dataSet[i, axis] == value:
            data = list(dataSet[i, :])
            example = data[:axis]
            example.extend(data[axis+1:])
            retDataSet.append(example)
            retWeight.append(weight[i])
    return array(retDataSet), array(retWeight)

def bestFeature(dataSet, weight):
    numberFeatures = dataSet.shape[1] - 1
    baseEnt = entropy(dataSet, weight)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numberFeatures):
        uniqueVals = set(dataSet[:, i])
        newEnt = 0.0
        for value in uniqueVals:
            dataSetSub, weightSub = dataSetProcess(dataSet, i, value, weight)
            prob = sum(weightSub) / sum(weight)
            newEnt += prob * entropy(dataSetSub, weightSub)
        infoGain = baseEnt - newEnt
        if infoGain >= bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature, bestInfoGain

def vote(labelList):
    x = len(labelList[labelList == -1])
    y = len(labelList[labelList == 1])
    if x >= y:
        return -1
    else:
        return 1

def decisionTree(dataSet, featuresLabels, weight):
    labelList = dataSet[:, -1]
    if len(set(labelList)) == 1:
        return labelList[0]
    if dataSet.shape[1] == 1:
        return vote(labelList)
    bestFeat, bestInfoGain = bestFeature(dataSet, weight)
    if bestInfoGain == 0:
        return vote(labelList)
    bestFeatLabel = featuresLabels[bestFeat]
    tree = {bestFeatLabel:{}}
    del(featuresLabels[bestFeat])
    uniqueVals = set(dataSet[:, bestFeat])
    for value in uniqueVals:
        subFeatLabels = featuresLabels[:]
        dataSetSub, weightSub = dataSetProcess(dataSet, bestFeat, value, weight)
        tree[bestFeatLabel][value] = decisionTree(dataSetSub, subFeatLabels, weightSub)
    return tree

def decisionTreeClassify(decisionTreeInput, testVector):
    if type(decisionTreeInput).__name__ == 'int':
        return decisionTreeInput
    featureIndex = list(decisionTreeInput.keys())[0]
    branchDict = decisionTreeInput[featureIndex]
    classLabel = 0
    for branch in branchDict:
        if testVector[featureIndex] == branch:
            if type(branchDict[branch]).__name__ == 'dict':
                classLabel = decisionTreeClassify(branchDict[branch], testVector)
            else:
                classLabel = branchDict[branch]
    return classLabel       

def adaboostTraining(trainDataSet):
    numIt = 1000
    labels = trainDataSet[:, -1]
    weakClassifier = []
    alpha = []
    m, n = trainDataSet.shape
    weight = array([1] * m) / m
    adaboostClassEst = array([0] * m)
    for i in range(numIt):
        error = 0
        classEst = arange(m)
        featuresLabels = list(arange(n-1))
        tree = decisionTree(trainDataSet, featuresLabels, weight)
        for j in range(m):
            classEst[j] = decisionTreeClassify(tree, trainDataSet[j, :])
            if classEst[j] != labels[j]:
                error += 1
        error = error / m
        alpha.append(0.5 * math.log((1 - error) / max(error, 1e-16)))
        weakClassifier.append(tree)
        expon = labels * classEst * (-alpha[i])
        weight = weight * exp(expon) / sum(weight)
        adaboostClassEst += alpha[i] * classEst
        errorRate = 0
        for j in range(m):
            if labels[j] * adaboostClassEst[j] < 0:
                errorRate += 1
        errorRate /= m
        if errorRate == 0:
            break
    return weakClassifier, alpha
        
def adaboostClassify(testDataSet, weakClassifier, alpha):
    m = testDataSet.shape[0]
    adaboostClassEst = array([0] * m)
    labels = testDataSet[:, -1]
    for i in range(len(weakClassifier)):
        classEst = array([0] * m)
        for j in range(m):
            classEst[j] = decisionTreeClassify(weakClassifier[i], testDataSet[j])
        adaboostClassEst += alpha[i] * classEst
    errorRate = 0
    for j in range(m):
        if labels[j] * adaboostClassEst[j] < 0:
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
        weakClassifier, alpha = adaboostTraining(trainDataSet)
        correctRate.append(1 - adaboostClassify(testDataSet, weakClassifier, alpha))
    return array(correctRate)

print("Adaboost Algorithm")
fileName = ["breast-cancer-assignment5.txt", "german-assignment5.txt"]
for item in range(len(fileName)):
    print("Processing the dataSet ", item + 1)
    dataSet = dataProcess(fileName[item], item)
    correctRate = _10foldCrossValidation(dataSet)
    print("The correct rate on dataSet " ,item + 1, "is: \n", correctRate)
    meanCorrect = mean(correctRate)
    stdCorrect = std(correctRate)
    print("The average on dataSet ", item + 1, "is: ", meanCorrect, "standard deviation on dataSet ", item + 1, "is: ", stdCorrect)








