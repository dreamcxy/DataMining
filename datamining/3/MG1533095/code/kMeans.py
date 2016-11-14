from __future__ import division
from numpy import *

def loadDataSet(fileName):
    dataMat = []
    label = []
    fr = open(fileName)
    for line in fr:
        line = line.split(',')
        data = [float(i) for i in line[:-1]]
        dataMat.append(data)
        label.append(int(line[-1]))
    fr.close()
    return array(dataMat), array(label)

def distEclid(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))

def initRep(dataSet, k, num):
    n = shape(dataSet)[1]
    rep = zeros((k,n))
    rep[0:k,:] = dataSet[k*num:k*num+k,:]
    return rep

def kMeans(fileName, k, num):
    dataSet, label = loadDataSet(fileName)
    m = shape(dataSet)[0]
    clusterResult = zeros((m,2))
    rep = initRep(dataSet, k, num)
    changed = True
    while changed:
        changed = False
        for i in range(m):
            minDist = inf; minIndex = -1
            for j in range(k):
                distJI = distEclid(rep[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterResult[i,0] != minIndex:
                changed = True
            clusterResult[i,:] = minIndex, minDist**2
        for i in range(k):
            dataInRep = dataSet[nonzero(clusterResult[:,0] == i)[0]]
            rep[i,:] = mean(dataInRep, axis=0)
    return clusterResult, label

def formConMat(clusterResult, label, k):
    conMat = zeros((k,k))
    L = label.copy()
    L = list(set(L))
    for i in range(k):
        for j in range(k):
            dataLabel = label[nonzero(clusterResult[:,0] == j)[0]]
            dataLabel = list(dataLabel)
            conMat[i,j] = dataLabel.count(L[i])
    return conMat

def purityCal(conMat):
    P = amax(conMat, axis=0)
    purity = sum(P)/sum(conMat)
    return purity

def giniCal(conMat):
    M = sum(conMat,axis=0)
    n = conMat.shape[1]
    G = zeros((1,n))
    for j in range(n):
        G[0,j] = 1-sum(power(conMat[:,j]/M[j],2))
    giniAve = sum(G*M)/sum(M)
    return giniAve

def main():
    k = [2,10]
    fileName = ["german.txt","mnist.txt"]
    for i in range(len(k)):
        SSE = inf; minIndex = -1
        for j in range(10):
            clusterResult, label = kMeans(fileName[i], k[i], j)
            SSEj = sum(clusterResult[:,1])
            if(SSEj<SSE):
                SSE = SSEj; minIndex = j
        clusterResult, label = kMeans(fileName[i], k[i], minIndex)
        conMat = formConMat(clusterResult, label, k[i])
        purity = purityCal(conMat)
        gini = giniCal(conMat)
        print(fileName[i],":")
        print("purity:",purity)
        print("gini:",gini)
        print("SEE",SSE)
        print(conMat)

main()
