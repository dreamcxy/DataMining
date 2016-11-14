import math
from numpy import *
import pickle

featProb = [ 0.00787535,  0.00817414,  0.00789243,  0.00804079,  0.00787459,
             0.00787812,  0.00787457,  0.0080534 ,  0.00790915,  0.00841103,
             0.00851936,  0.00788336,  0.007899  ,  0.00792859,  0.0078595 ,
             0.00788615,  0.00789727,  0.00790231,  0.00790037,  0.00787489,
             0.00787669,  0.00791117,  0.00794233,  0.00790945,  0.00787459,
             0.00793403,  0.0078746 ,  0.00787445,  0.0079834 ,  0.00787469,
             0.00787466,  0.00787474,  0.00789513,  0.00845025,  0.00761155,
             0.00831595,  0.00748554,  0.0078465 ,  0.00787549,  0.00787598,
             0.00811157,  0.00789324,  0.00797655,  0.00787742,  0.00788233,
             0.00789232,  0.00797179,  0.00787925,  0.00789273,  0.0079471 ,
             0.00787886,  0.00819599,  0.0079502 ,  0.00789584,  0.00790705,
             0.00787882,  0.0078982 ,  0.00788367,  0.00788346,  0.00821937,
             0.0081957 ,  0.00787453,  0.00787438,  0.00790265,  0.00790891,
             0.00789859,  0.00792702,  0.00788321,  0.00964653,  0.00792543,
             0.00788232,  0.00788247,  0.00787459,  0.00787841,  0.00788806,
             0.00807255,  0.00794377,  0.00788048,  0.00790604,  0.00787514,
             0.00814977,  0.00787914,  0.00787559,  0.00787464,  0.0078761 ,
             0.00787464,  0.00788061,  0.00788513,  0.00787695,  0.00787965,
             0.0078782 ,  0.0078762 ,  0.00815324,  0.00788446,  0.00787473,
             0.00788016,  0.00787948,  0.0078747 ,  0.00787623,  0.007883  ,
             0.00792587,  0.0078951 ,  0.00791574,  0.00787518,  0.00788328,
             0.00787706,  0.00787586,  0.00787658,  0.00788424,  0.00787452,
             0.00787909,  0.00787822,  0.0078803 ,  0.00787946,  0.00790026,
             0.00790915,  0.00787487,  0.00789789,  0.00787476,  0.0079093 ,
             0.00788616,  0.00787586,  0.00787463,  0.0078863 ,  0.0078888 ,
             0.0079768]

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

def calUniqueVals(dataSet):
    m, n = dataSet.shape
    uniqueVals = [0] * (n - 2)
    for j in range(1, n-1):
        uniqueVals[j - 1] = set(dataSet[:, j])
    return uniqueVals


##def calEntropy(dataSet):
##    #计算熵,分成两类：1和-1
##    m, n = dataSet.shape
##    classLabels = dataSet[:, n - 1]
##    prob1 = len(classLabels[classLabels == -1]) / m
##    prob2 = 1 - prob1
##    if prob1 < 1e-5 or prob2 < 1e-5:
##        return 0
##    return -prob1 * math.log(prob1, 2) - prob2 * math.log(prob2, 2)

def calEntropy(dataSet):
    #计算熵，分成多类
    m, n = dataSet.shape
    classLabel = dataSet[:, -1]
    labelCount = {}
    for i in range(m):
        label = classLabel[i]
        labelCount[label] = labelCount.get(label, 0) + 1
    entropy = 0
    for label in labelCount:
        prob = labelCount[label] / m
        if prob < 1e-5:
            continue
        entropy -= prob * math.log(prob, 2)
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

def bestFeature(dataSet, featRange, uniqueVals):
    #选择最佳的特征，用来划分数据集
    numFeatures = len(featRange)
    baseEntropy = calEntropy(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        newEntropy = 0.0
        for value in uniqueVals[featRange[i]]:
            subDataSet = splitDataSet(dataSet, featRange[i], value)
            if len(subDataSet) == 0:
                continue
            prob = len(subDataSet) / len(dataSet)
            newEntropy += prob * calEntropy(subDataSet)
        infoGain = baseEntropy - newEntropy
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = featRange[i]
    return bestFeature

##def majorCount(labelList):
##	#投票，采取众数决定类标签
##    x = len(labelList[labelList == -1])
##    y = len(labelList[labelList == 1])
##    if x >= y:
##        return -1
##    else:
##        return 1

def majorCount(labelList):
    labelCount = {}
    for label in labelList:
        labelCount[label] = labelCount.get(label, 0) + 1
    sortedLabelCount = sorted(labelCount.items(), key = lambda e:e[1], reverse = True)
    return sortedLabelCount[0][0]

def createTree(dataSet, uniqueVals):
    #创建决策树
    #print("正在建立决策树")
    labelList = dataSet[:, -1]
    label = majorCount(labelList)
    if len(set(labelList)) == 1:
        return labelList[0]
    n = dataSet.shape[1]
    featRange = list(random.choice(126, 15, replace = False, p = featProb))    #################
    bestFeat = bestFeature(dataSet, featRange, uniqueVals)
    if bestFeat == -1:
        return label
    if len(set(dataSet[:, bestFeat])) == 1:
        return label
    tree = {bestFeat:{}}
    for value in uniqueVals[bestFeat]:
        subDataSet = splitDataSet(dataSet, bestFeat, value)
        if len(subDataSet) == 0:
            tree[bestFeat][value] = label
        else:
            tree[bestFeat][value] = createTree(subDataSet, uniqueVals)
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
				
def sample(dataSet):  ###################################
    #采用有放回抽样生成新的数据
    m = dataSet.shape[0]
    classLabels = dataSet[:, -1]
    indexs = []
    retData = []
    for i in range(m):
        data = list(dataSet[i, :])
        if classLabels[i] == 3:
            for k in range(5):
                retData.append(data)
        elif classLabels[i] == 4:
            for k in range(4):
                retData.append(data)
        elif classLabels[i] == 8:
            for k in range(random.randint(2)):
                retData.append(data)
        else:
            retData.append(data)
    return array(retData)

def forestTrain(trainDataSet, uniqueVals):
    #使用随机森林算法训练分类器
    treeNum = 1                                ################
    weakClassifier = []
    for i in range(treeNum):
        dataSet = sample(trainDataSet)
        print("正在建第",i,"棵树")
        tree = createTree(dataSet, uniqueVals)
        print("第",i,"棵树已经建好")
        weakClassifier.append(tree)
        storeTree(tree, "TR" + str(i+1) + ".txt") ###################
    return weakClassifier

##def forestClassify(testDataSet, weakClassifier):
##    #使用随机森林分类器测试数据
##    print("正在测试随机森林")
##    m = testDataSet.shape[0]
##    aggClassEst = []
##    classLabels = testDataSet[:, -1]
##    for j in range(m):
##        classEst = []
##        for i in range(len(weakClassifier)):
##            classEst.append(treeClassify(weakClassifier[i], testDataSet[j, :]))
##        aggClassEst.append(majorCount(classEst))
##    print("len(aggClassEst)",len(aggClassEst))
##    errorRate = 0
##    for j in range(m):
##        if classLabels[j] != aggClassEst[j]:
##            #print("j",j,"classLabels[j]",classLabels[j],"aggClassEst[j]",aggClassEst[j])
##            errorRate += 1
##    errorRate /= m
##    return errorRate

def main():
    #主程序
    dataSet = loadDataSet("train.txt")
    uniqueVals = calUniqueVals(dataSet)
    dataSet = dataSet[:, 1:].copy()
    weakClassifier = forestTrain(dataSet, uniqueVals)
##    m, n = dataSet.shape
##    classCount = {}
##    for i in range(m):
##        label = int(dataSet[i, -1])
##        classCount[label] = classCount.get(label, 0) + 1
##    for i in range(1, 9):
##        print("i:", i, "label:", classCount[i], int(classCount[i] / m * 19765))

def test():
    dataSet = loadDataSet("test.txt")
    idNum = dataSet[:, 0]
    dataSet = dataSet[:, 1:].copy()
    m, n = dataSet.shape
    treeNum = 1   ################
    classLabels = []
    weakClassifier = []
    for i in range(treeNum):
        tree = grabTree("TR" + str(i+1) + ".txt")
        weakClassifier.append(tree)
    for i in range(m):
        classEst = []
        if i % 1000 ==0:
            print("正在测试第", i, "条数据")
        for j in range(treeNum):
            classEst.append(treeClassify(weakClassifier[j], dataSet[i, :]))
        classLabels.append(majorCount(classEst))
    fw = open("result.csv", 'w')
    fw.write("\"Id\",\"Response\"\n")
    classCount = {}
    for i in range(m):
        fw.write("%d,%d\n" % (int(idNum[i]), int(classLabels[i])))
        classCount[int(classLabels[i])] = classCount.get(int(classLabels[i]), 0) + 1
    fw.close()
    for i in range(1, 9):
        print("i:", i, "label:", classCount[i])

#main()

test()
        
##dataSet = loadDataSet("test.txt")
##dataSet = dataSet[:, 1:].copy()
##weakClassifier = []
##for i in range(7):
##    tree = grabTree("TR" + str(i+1) + ".txt")
##    weakClassifier.append(tree)
##x=treeClassify(weakClassifier[6], dataSet[9611, :])
##print(x)


















