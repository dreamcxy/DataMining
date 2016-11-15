from __future__ import division
from numpy import *
import random
from math import e

def loadDataSet(fileName):
    dataMat = []
    label = []
    fr = open(fileName)
    for line in fr:
        line = line.split(',')
        data = [int(i) for i in line]
        dataMat.append(data[:-1])
        label.append(data[-1])
    fr.close()
    return array(dataMat), array(label)

def log(fileName, lamda, num):
    feature, label = loadDataSet(fileName)
    m, n = feature.shape
    w = array([0] * n)
    for t in range(num):
        i = random.randint(0, m-1)
        enda = 1/(lamda * (t+1))
        if sum(w * feature[i, :]) * label[i] < 1:
            w = (1 - enda * lamda) * w + enda * label[i] * feature[i, :]
        else:
            w = (1 - enda * lamda) * w
    return w

def ridge(fileName, lamda, num):
    feature, label = loadDataSet(fileName)
    m, n = feature.shape
    w = array([0] * n, dtype = float)
    for t in range(num):
        i = random.randint(0, m-1)
        enda = 1/(lamda * (t+1))
        z = sum(w * feature[i, :])
        w = (1 - enda * lamda) * w + enda * label[i] / (1 + e**(label[i] * z)) * feature[i, :]
    return w

def test(fileName, w):
    testFeature, testLabel = loadDataSet(fileName)
    m, n = testFeature.shape
    correct = 0
    for i in range(m):
        if sum(w * testFeature[i, :]) * testLabel[i] > 0:
            correct += 1
    return 1 - correct/m

def main():
    trainingFileName = ["training1.txt", "training2.txt"]
    testFileName = ["testing1.txt", "testing2.txt"]
    lamda = [1e-4, 5e-5]
    T = [113480, 162805]
    radio_test = []
    radio_train = []
    # for j in range(1,100):
    #     # w = log(trainingFileName[i], lamda[i], int(T[i] / 10 * (j + 1)))
    #     w = log(trainingFileName[1], lamda[1], int(j*100))
    #     print test(trainingFileName[1], w)
    #     radio.append(test(testFileName[1], w))
    # print(radio)
    for i in range(1, 100):
        w = ridge(trainingFileName[1], lamda[0], int(i*100))
        radio_train.append(test(trainingFileName[1], w))
        radio_test.append(test(testFileName[1], w))
    print radio_train
    print radio_test

main()
