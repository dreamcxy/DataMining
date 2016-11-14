import math
from numpy import *

def loadDataSet(fileName, fileNum):
	#载入数据
    print("正在载入数据", fileNum + 1, fileName)
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
            x = random.randint(1, 278)
            dataSet.append(dataSet[x])
    dataSet = array(dataSet[1:])
    m = dataSet.shape[0]
    if fileNum == 1:
        for j in range(12):
            if len(set(dataSet[:, j])) > 3:
                rangeMin = min(dataSet[:, j])
                rangeMax = max(dataSet[:, j]) + 0.01
                rangeX = linspace(rangeMin, rangeMax, 4)
                for i in range(m):
                    for k in range(3):
                        if rangeX[k] <= dataSet[i,j] < rangeX[k+1]:
                            dataSet[i, j] = k
    return dataSet

def calEntropy(dataSet, weight):
	#计算熵
    classLabels = dataSet[:, -1]
    prob1 = sum(weight[classLabels == -1]) / sum(weight)
    prob2 = sum(weight[classLabels == 1]) / sum(weight)
    if prob1 < 1e-5 or prob2 < 1e-5:
        return 0
    entropy = -prob1 * math.log(prob1, 2) - prob2 * math.log(prob2, 2)
    return entropy

def splitDataSet(dataSet, axis, value, weight):
	#划分数据集
    retDataSet = []
    retWeight = []
    m = dataSet.shape[0]
    for i in range(m):
        if dataSet[i, axis] == value:
            data = list(dataSet[i, :])
            reducedExample = data[:axis]
            reducedExample.extend(data[axis+1:])
            retDataSet.append(reducedExample)
            retWeight.append(weight[i])
    return array(retDataSet), array(retWeight)

def bestFeature(dataSet, weight):
	#选择最佳的特征，用来划分数据集
    numFeatures = dataSet.shape[1] - 1
    baseEntropy = calEntropy(dataSet, weight)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        uniqueVals = set(dataSet[:, i])
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet, subWeight = splitDataSet(dataSet, i, value, weight)
            prob = sum(subWeight) / sum(weight)
            newEntropy += prob * calEntropy(subDataSet, subWeight)
        infoGain = baseEntropy - newEntropy
        if infoGain >= bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature, bestInfoGain

def majorCount(labelList):
	#投票，采取众数决定类标签
    x = len(labelList[labelList == -1])
    y = len(labelList[labelList == 1])
    if x >= y:
        return -1
    else:
        return 1

def createTree(dataSet, featLabels, weight):
	#创建决策树
    labelList = dataSet[:, -1]
    if len(set(labelList)) == 1:
        return labelList[0]
    if dataSet.shape[1] == 1:
        return majorCount(labelList)
    bestFeat, bestInfoGain = bestFeature(dataSet, weight)
    if bestInfoGain == 0:
        return majorCount(labelList)
    bestFeatLabel = featLabels[bestFeat]
    tree = {bestFeatLabel:{}}
    del(featLabels[bestFeat])
    uniqueVals = set(dataSet[:, bestFeat])
    for value in uniqueVals:
        subFeatLabels = featLabels[:]
        subDataSet, subWeight = splitDataSet(dataSet, bestFeat, value, weight)
        tree[bestFeatLabel][value] = createTree(subDataSet, subFeatLabels, subWeight)
    return tree

def treeClassify(inputTree, testVect):
	#使用决策树进行分类
    if type(inputTree).__name__ == 'int':
        return inputTree
    featIndex = list(inputTree.keys())[0]
    branchDict = inputTree[featIndex]
    classLabel = 0
    for branch in branchDict:
        if testVect[featIndex] == branch:
            if type(branchDict[branch]).__name__ == 'dict':
                classLabel = treeClassify(branchDict[branch], testVect)
            else:
                classLabel = branchDict[branch]
    return classLabel       

def adaTrain(trainDataSet):
	#使用adaboost算法训练分类器
    numIt = 1000
    classLabels = trainDataSet[:, -1]
    weakClassifier = []
    alpha = []
    m, n = trainDataSet.shape
    weight = array([1] * m) / m
    adaClassEst = array([0] * m)
    for i in range(numIt):
        error = 0
        classEst = arange(m)
        featLabels = list(arange(n-1))
        tree = createTree(trainDataSet, featLabels, weight)
        for j in range(m):
            classEst[j] = treeClassify(tree, trainDataSet[j, :])
            if classEst[j] != classLabels[j]:
                error += 1
        error = error / m
        alpha.append(0.5 * math.log((1 - error) / max(error, 1e-16)))
        weakClassifier.append(tree)
        expon = classLabels * classEst * (-alpha[i])
        weight = weight * exp(expon) / sum(weight)
        adaClassEst += alpha[i] * classEst
        errorRate = 0
        for j in range(m):
            if classLabels[j] * adaClassEst[j] < 0:
                errorRate += 1
        errorRate /= m
        if errorRate == 0:
            break
    return weakClassifier, alpha
        
def adaClassify(testDataSet, weakClassifier, alpha):
	#使用adaboost分类器测试数据
    m = testDataSet.shape[0]
    adaClassEst = array([0] * m)
    classLabels = testDataSet[:, -1]
    for i in range(len(weakClassifier)):
        classEst = array([0] * m)
        for j in range(m):
            classEst[j] = treeClassify(weakClassifier[i], testDataSet[j])
        adaClassEst += alpha[i] * classEst
    errorRate = 0
    for j in range(m):
        if classLabels[j] * adaClassEst[j] < 0:
            errorRate += 1
    errorRate /= m
    return errorRate

def crossValidation(dataSet):
	#10折交叉验证
    correctRate = []
    m = dataSet.shape[0]
    step = m / 10
    allSet = set(arange(m))
    for fold in range(10):
        testSet = set(arange(fold * step, (fold + 1) * step))
        trainSet = allSet - testSet
        testDataSet = dataSet[list(testSet), :]
        trainDataSet = dataSet[list(trainSet), :]
        print("正在数据集", fold, "上使用adaboost算法训练分类器：")
        weakClassifier, alpha = adaTrain(trainDataSet)
        correctRate.append(1 - adaClassify(testDataSet, weakClassifier, alpha))
    return array(correctRate)

def main():
	#主程序
    fileName = ["breast-cancer-assignment5.txt", "german-assignment5.txt"]
    for i in range(len(fileName)):
        dataSet = loadDataSet(fileName[i], i)
        correctRate = crossValidation(dataSet)
        print("正确率：\n", correctRate)
        meanCorrect = mean(correctRate)
        stdCorrect = std(correctRate)
        print("平均值：", meanCorrect, "标准差：", stdCorrect)

main()
#按F5直接运行程序，无需其他操作


def calEntropy(dataSet):
    #计算熵
    m, n = dataSet.shape
    classLabels = dataSet[:, n - 1]
    prob1 = len(classLabels[classLabels == -1]) / m
    prob2 = 1 - prob1
    if prob1 < 1e-5 or prob2 < 1e-5:
        return 0
    entropy = -prob1 * math.log(prob1, 2) - prob2 * math.log(prob2, 2)
    return entropy

def splitDataSet(dataSet, axis, value, uniqueVals):
    #划分数据集
    retDataSet = []
    retUniqueVals = []
    m, n = dataSet.shape
    for j in range(n-1):
        if j != axis:
            retUniqueVals.append(uniqueVals[j])
    for i in range(m):
        if dataSet[i, axis] == value:
            data = list(dataSet[i, :])
            reducedExample = data[:axis]
            reducedExample.extend(data[axis+1:])
            retDataSet.append(reducedExample)
    return array(retDataSet), retUniqueVals

def bestFeature(dataSet, uniqueVals):
    #选择最佳的特征，用来划分数据集
    numFeatures = dataSet.shape[1] - 1
    baseEntropy = calEntropy(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        newEntropy = 0.0
        for value in uniqueVals[i]:
            subDataSet, subUniqueVals = splitDataSet(dataSet, i, value, uniqueVals)
            if len(subDataSet) == 0:
                continue
            prob = len(subDataSet) / len(dataSet)
            newEntropy += prob * calEntropy(subDataSet)
        infoGain = baseEntropy - newEntropy
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def majorCount(labelList):
    #投票，采取众数决定类标签
    x = len(labelList[labelList == -1])
    y = len(labelList[labelList == 1])
    if x >= y:
        return -1
    else:
        return 1

def createTree(dataSet, featLabels, uniqueVals):
    #创建决策树
    labelList = dataSet[:, -1]
    label = majorCount(labelList)
    if len(set(labelList)) == 1:
        return labelList[0]
    if dataSet.shape[1] == 1:
        return label
    bestFeat = bestFeature(dataSet, uniqueVals)
    if bestFeat == -1:
        return label
    bestFeatLabel = featLabels[bestFeat]
    tree = {bestFeatLabel:{}}
    del(featLabels[bestFeat])
    for value in uniqueVals[bestFeat]:
        subFeatLabels = featLabels[:]
        subDataSet, subUniqueVals = splitDataSet(dataSet, bestFeat, value, uniqueVals)
        if len(subDataSet) == 0:
            tree[bestFeatLabel][value] = label
        else:
            tree[bestFeatLabel][value] = createTree(subDataSet, subFeatLabels, subUniqueVals)
    return tree

def treeClassify(inputTree, testVect):
    #使用决策树进行分类
    if type(inputTree).__name__ == 'int':
        return inputTree
    featIndex = list(inputTree.keys())[0]
    branchDict = inputTree[featIndex]
    for branch in branchDict:
        if testVect[featIndex] == branch:
            if type(branchDict[branch]).__name__ == 'dict':
                return treeClassify(branchDict[branch], testVect)
            else:
                return branchDict[branch]





