from __future__ import division
from numpy import *
from scipy import linalg as LA

def loadDataSet(fileName):
	#load text file
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

def dist(vecA, vecB):
	#calculate distance between vectors
    # return sum(power(vecA - vecB, 2))
    return linalg.norm((vecA - vecB), 1)

def distanceCal(fileName):
	#cal dis bet points
    dataSet, label = loadDataSet(fileName)
    m = dataSet.shape[0]
    Distance = zeros((m,m))
    for i in range(m-1):
        for j in range(i+1,m):
            Distance[i,j] = Distance[j,i] = dist(dataSet[i,:], dataSet[j,:])
        #print("dis",i)
    print("Distance calculated!")
    return Distance, label

def formW(Distance, n):
	#cal nei-Matrix
    m = Distance.shape[0]
    W = zeros((m, m))
    for i in range(m):
        D = Distance[i,:].copy()
        D = argsort(D)
        for j in range(1,n+1):
            W[i, D[j]] = W[D[j], i] = 1
        #print("W",i)
    return W

def EignMaps(Distance, n, k):
#  cal low-diverse matrix
    W = formW(Distance, n)
    m = W.shape[0]
    D = zeros((m,m))
    L = zeros((m,m))
    dataSet = zeros((m,k))
    for i in range(m):
        D[i,i] = sum(W[i,:])
    L = D - W
    for i in range(m):
        D[i,i] = 1/D[i,i]
    L = dot(D, L)
    #print("here")
    value, vector = LA.eig(L)
    v = (value.real).copy()
    v = argsort(v)
    #print("vector 1:",vector[0:1000,v[0]])#
    for i in range(k):
        dataSet[:,i] = vector[:,v[i+1]].real
    return dataSet

def initRep(dataSet, k, num):
	#init represent 
    n = shape(dataSet)[1]
    rep = zeros((k,n))
    rep[0:k,:] = dataSet[k*num:k*num+k,:]
    return rep

def kMeans(dataSet, k, num):
	#use kMeans
    m = shape(dataSet)[0]
    clusterResult = zeros((m,2))
    rep = initRep(dataSet, k, num)
    changed = True
    while changed:
        changed = False
        for i in range(m):
            minDist = inf; minIndex = -1
            for j in range(k):
                distJI = dist(rep[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterResult[i,0] != minIndex:
                changed = True
            clusterResult[i,:] = minIndex, minDist
        for i in range(k):
            dataInRep = dataSet[nonzero(clusterResult[:,0] == i)[0]]
            rep[i,:] = mean(dataInRep, axis=0)
    return clusterResult

def formConMat(clusterResult, label, k):
    #form matrix
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
	#cal purity
    P = amax(conMat, axis=0)
    purity = sum(P)/sum(conMat)
    return purity

def giniCal(conMat):
	#cal gini
    M = sum(conMat,axis=0)
    n = conMat.shape[1]
    G = zeros((1,n))
    for j in range(n):
        G[0,j] = 1-sum(power(conMat[:,j]/M[j],2))
    giniAve = sum(G*M)/sum(M)
    return giniAve

def main():
	#main
    k = [2,10]
    fileName = ["german.txt","mnist.txt"]
    n = [3,6,9]
    for i in range(len(k)):
        Distance, label = distanceCal(fileName[i])
        for ii in range(len(n)):
            dataSet = EignMaps(Distance, n[ii], k[i])
            SSE = inf
            clusterResult = array([])
            for j in range(10):
                clusterResultTemp = kMeans(dataSet, k[i], j)
                SSEj = sum(clusterResultTemp[:,1])
                if(SSEj < SSE):
                    SSE = SSEj
                    clusterResult = clusterResultTemp
            conMat = formConMat(clusterResult, label, k[i])
            purity = purityCal(conMat)
            gini = giniCal(conMat)
            print(fileName[i],":(n=",n[ii],")")
            print("SSE:",SSE)
            print("purity:",purity)
            print("gini:",gini)
            print(conMat)

main()




















