import math
from math import e
from numpy import *
import pickle

def loadDataSet(fileName):
    #载入数据
    print("正在载入数据", fileName)
    dataSet = []
    fr = open(fileName)
    for line in fr:
        line = line.strip()
        line = line.split(',')
        data = [float(i) for i in line]
        dataSet.append(data)
    fr.close()
    return array(dataSet)

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

def grabTree(fileName):
    fr = open("result\\" + fileName, 'rb')
    tree = pickle.load(fr)
    fr.close()
    return tree

def adaTrain(dataSet, weakClassifier):
    #使用adaboost算法训练分类器
    print("正在使用adaboost算法训练分类器")
    numIt = 180  #####################
    classLabels = dataSet[:, -1]
    alpha = []
    label = []
    retWeakClassifier = []
    m, n = dataSet.shape
    weight = array([1] * m) / m
    adaClassEst = zeros((m, 2))
    for k in range(len(weakClassifier)):
        classEst = [0] * m
        for j in range(m):
            classEst[j] = treeClassify(weakClassifier[k], dataSet[j, :])
        label.append(classEst)
    for i in range(numIt):
        print("numIt:",i)
        weightedError = inf
        treeIndex = inf
        for k in range(len(weakClassifier)):
            newWeightedError = 0
            classEst = label[k]
            for j in range(m):
                if classEst[j] != classLabels[j]:
                    newWeightedError += weight[j]
            newWeightedError *= e
            if newWeightedError < weightedError:
                weightedError = newWeightedError
                treeIndex = k
        alphaTemp = 0.5 * math.log((1 - weightedError) / max(weightedError, 1e-16))
        if alphaTemp <= 0:
            continue
        print("Found!!!")
        retWeakClassifier.append(weakClassifier[treeIndex])
        alpha.append(ahphaTemp)
        expon = classLabels * label[treeIndex] * (-alpha[i])
        weight = weight * exp(expon)
        weight = weight / sum(weight)
        for j in range(m):
            if adaClassEst[j, 0] == label[j]:
                adaClassEst[j, 1] += alpha[i]
            else:
                if adaClassEst[j, 1] < alpha[i]:
                    adaClassEst[j, 0] = label[j]
                    adaClassEst[j, 1] = alpha[i]
        errorRate = 0
        for j in range(m):
            if classLabels[j] != adaClassEst[j, 0]:
                errorRate += 1
        errorRate /= m
        print("errorRate",errorRate)
        if errorRate == 0:
            break
    return retWeakClassifier, alpha
        
def adaClassify(testDataSet, weakClassifier, alpha):
    #使用adaboost分类器测试数据
    m = testDataSet.shape[0]
    adaClassEst = zeros((m, 2))
    for i in range(len(weakClassifier)):
        label = array([0] * m)
        print("正在测试第", i, "个分类器")
        for j in range(m):
            label[j] = treeClassify(weakClassifier[i], testDataSet[j, :])
            if adaClassEst[j, 0] == label[j]:
                adaClassEst[j, 1] += alpha[i]
            else:
                if adaClassEst[j, 1] < alpha[i]:
                    adaClassEst[j, 0] = label[j]
                    adaClassEst[j, 1] = alpha[i]
    return adaClassEst

def main():
    #主程序
    dataSet = loadDataSet("train.txt")
    dataSet = dataSet[:, 1:].copy()
    treeNum = 184   ################
    weakClassifier = []
    for i in range(treeNum):
        tree = grabTree("TR" + str(i+1) + ".txt")
        weakClassifier.append(tree)
    choosenWeakClassifier, alpha = adaTrain(dataSet, weakClassifier)
    testDataSet = loadDataSet("test.txt")
    idNum = testDataSet[:, 0]
    testDataSet = testDataSet[:, 1:].copy()
    m, n = testDataSet.shape
    adaClassEst = adaClassify(testDataSet, choosenWeakClassifier, alpha)
    fw = open("resultAda.csv", 'w')
    fw.write("\"Id\",\"Response\"\n")
    for i in range(m):
        fw.write("%d,%d\n" %(int(idNum[i]), int(adaClassEst[i, 0])))
    fw.close()


main()








