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

def hinge(fileName, lamda, num):
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

def log(fileName, lamda, num):
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
    trainingFileName = ["dataset1-a8a-training.txt", "dataset1-a9a-training.txt"]
    testFileName = ["dataset1-a8a-testing.txt", "dataset1-a9a-testing.txt"]
    lamda = [1e-4, 5e-5]
    T = [113480, 162805]
    for i in range(2):
        print("dataset", str(i+1), ",hinge function:")
        radio = []
        for j in range(1,100):
            # w = hinge(trainingFileName[i], lamda[i], int(T[i] / 10 * (j + 1)))
            w = hinge(trainingFileName[i], lamda[i], int(i*100))
            radio.append(test(testFileName[i], w))
        print(radio)
    for i in range(2):
        print("dataset", str(i+1), ",log function:")
        radio = []
        for j in range(1,10):
            w = log(trainingFileName[i], lamda[i], int(i*100))
            radio.append(test(testFileName[i], w))
        print(radio)

main()
