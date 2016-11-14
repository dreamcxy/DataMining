import math
from math import e
from numpy import *
import pickle

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

def storeTree(inputTree, fileName):
    fw = open("result\\" + fileName, 'wb')
    pickle.dump(inputTree, fw)
    fw.close()

def grabTree(fileName):
    fr = open("result\\" + fileName, 'rb')
    tree = pickle.load(fr)
    fr.close()
    return tree

def adaTrain(dataSet, uniqueVals):
    #使用adaboost算法训练分类器
    numIt = 6
    classLabels = dataSet[:, -1]
    weakClassifier = []
    alpha = []
    m, n = dataSet.shape
    weight = array([1] * m) / m
    adaClassEst = array([0] * m)
    classEst = arange(m)
    trainDataSet = copy(dataSet)
    for i in range(numIt):
        print("numIt:",i)
        weightedError = 0
        error =0#
        featLabels = list(arange(n-1))
        tree = createTree(trainDataSet, featLabels, uniqueVals)
        storeTree(tree, "TR" + str(i) + ".txt")#
        weakClassifier.append(tree)
        for j in range(m):
            classEst[j] = treeClassify(weakClassifier[i], dataSet[j, :])
            if classEst[j] != classLabels[j]:
                #print(j,"classEst[j]",classEst[j],"classLabels[j]",classLabels[j],"weight[j]",weight[j])
                weightedError += weight[j]
                error += 1#
        error /= m#
        print("error:",error)#
        #print("classEst",classEst)
        weightedError *= e
        alpha.append(0.5 * math.log((1 - weightedError) / max(weightedError, 1e-16)))
        print("weightedError:",weightedError,"alpha:",alpha[i])
        expon = classLabels * classEst * (-alpha[i])
        weight = weight * exp(expon)
        weight = weight / sum(weight)
        adaClassEst = adaClassEst + alpha[i] * classEst
        indices = random.choice(m, m, replace = True, p = weight)
        trainDataSet = dataSet[indices, :]
        errorRate = 0
        for j in range(m):
            if classLabels[j] * adaClassEst[j] < 0:
                #print("classLabels[j]",classLabels[j],"adaClassEst[j]",adaClassEst[j])
                errorRate += 1
        #print("errorNum:", errorRate)
        errorRate /= m
        print("errorRate",errorRate)
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
        adaClassEst = adaClassEst + alpha[i] * classEst
    errorRate = 0
    for j in range(m):
        if classLabels[j] * adaClassEst[j] < 0:
            errorRate += 1
    errorRate /= m
    return errorRate

def main():
    #主程序
    fileName = ["breast-cancer-assignment5.txt"]
    #, "german-assignment5.txt"
    for i in range(len(fileName)):
        dataSet = loadDataSet(fileName[i], i)
        m, n = dataSet.shape
        uniqueVals = []
        for j in range(n-1):
            uniqueVals.append(set(dataSet[:, j]))
        weakClassifier, alpha = adaTrain(dataSet[0:250, :], uniqueVals)
##        for j in range(len(weakClassifier)):
##            tree = grabTree("TR" + str(j) + ".txt")
##            print(tree)
        #print("正确率：\n", correctRate)

main()
#按F5直接运行程序，无需其他操作








