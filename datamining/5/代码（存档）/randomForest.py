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
            if len(set(dataSet[:, j])) > 4:
                rangeMin = min(dataSet[:, j])
                rangeMax = max(dataSet[:, j]) + 0.01
                rangeX = linspace(rangeMin, rangeMax, 5)
                for i in range(m):
                    for k in range(4):
                        if rangeX[k] <= dataSet[i,j] < rangeX[k+1]:
                            dataSet[i, j] = k
    return dataSet

def calEntropy(dataSet):
	#计算熵
    m = dataSet.shape[0]
    classLabels = dataSet[:, -1]
    prob1 = len(classLabels[classLabels == -1]) / m
    prob2 = 1 - prob1
    if prob1 < 1e-5 or prob2 < 1e-5:
        return 0
    entropy = -prob1 * math.log(prob1, 2) - prob2 * math.log(prob2, 2)
    return entropy

def splitDataSet(dataSet, axis, value):
	#划分数据集
    retDataSet = []
    m = dataSet.shape[0]
    for i in range(m):
        if dataSet[i, axis] == value:
            data = list(dataSet[i, :])
            retDataSet.append(data)
    return array(retDataSet)

def bestFeature(dataSet, featRange):
	#选择最佳的特征，用来划分数据集
    numFeatures = len(featRange)
    baseEntropy = calEntropy(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        uniqueVals = set(dataSet[:, featRange[i]])
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, featRange[i], value)
            prob = len(subDataSet) / len(dataSet)
            newEntropy += prob * calEntropy(subDataSet)
        infoGain = baseEntropy - newEntropy
        if infoGain >= bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = featRange[i]
    return bestFeature, bestInfoGain

def majorCount(labelList):
	#投票，采取众数决定类标签
    x = len(labelList[labelList == -1])
    y = len(labelList[labelList == 1])
    if x >= y:
        return -1
    else:
        return 1

def createTree(dataSet):
	#创建决策树
    labelList = dataSet[:, -1]
    if len(set(labelList)) == 1:
        return labelList[0]
    n = dataSet.shape[1]
    featNum = int(math.sqrt(n-1))
    featRange = []
    while True:
        x = random.randint(n-1)
        if x not in featRange:
            featRange.append(x)
        if len(featRange) == featNum:
            break
    bestFeat, bestInfoGain = bestFeature(dataSet, featRange)
    if bestInfoGain == 0:
        return majorCount(labelList)
    if len(set(dataSet[:, bestFeat])) == 1:
        return majorCount(labelList)
    tree = {bestFeat:{}}
    uniqueVals = set(dataSet[:, bestFeat])
    for value in uniqueVals:
        subDataSet = splitDataSet(dataSet, bestFeat, value)
        tree[bestFeat][value] = createTree(subDataSet)
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

def sample(dataSet):
	#采用有放回抽样生成新的数据
    m = dataSet.shape[0]
    indices = list(random.randint(m, size = m))
    return dataSet[indices, :]

def forestTrain(trainDataSet):
	#使用随机森林算法训练分类器
    treeNum = 1000
    weakClassifier = []
    for i in range(treeNum):
        dataSet = sample(trainDataSet)
        tree = createTree(dataSet)
        weakClassifier.append(tree)
    return weakClassifier

def forestClassify(testDataSet, weakClassifier):
	#使用随机森林分类器测试数据
    m = testDataSet.shape[0]
    aggClassEst = array([0] * m)
    classLabels = testDataSet[:, -1]
    for i in range(len(weakClassifier)):
        classEst = array([0] * m)
        for j in range(m):
            classEst[j] = treeClassify(weakClassifier[i], testDataSet[j])
        aggClassEst += classEst
    errorRate = 0
    for j in range(m):
        if classLabels[j] * aggClassEst[j] < 0:
            errorRate += 1
        if aggClassEst[j] == 0:
            if classLabels[j] == -1:
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
        print("正在数据集", fold, "上使用随机森林算法训练分类器：")
        weakClassifier = forestTrain(trainDataSet)
        correctRate.append(1 - forestClassify(testDataSet, weakClassifier))
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






















