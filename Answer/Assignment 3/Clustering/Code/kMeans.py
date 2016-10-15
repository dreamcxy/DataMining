import math
import random
import numpy
import copy

clusterAssment = []

def distEnclud(vecA, vecB):
    dist = 0
    for i in range(0, len(vecA)-1):
        dist += pow(vecA[i] - vecB[i], 2)
    return dist

def randCent(length, k, method=0):
    centroids = []
    if method == 1:
        division = 20
    else:
        division = 1
    for i in range(0, k):
        b = []
        for j in range(0, length):
            b.append(random.uniform(-1, 1)/float(division))
        centroids.append(b)
    return centroids


def kMeans(vec, k, method=0):
    global clusterAssment
    centroids = randCent(len(vec[0])-1, k, method)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        clusterTemp = []
        for item in vec:
            minDist = []
            for cent in centroids:
                a = distEnclud(item, cent)
                minDist.append(a)
            i = 0
            for j in range(1, len(minDist)): 
                if minDist[i] > minDist[j]:
                    i = j
            clusterTemp.append(i) 

        cal = []
        for i in range(0, len(vec[0])-1):
            cal.append(0)

        for i in range(0, k):
            cnt = 0
            for j in range(0, len(vec)):
                if clusterTemp[j] == i:
                    cnt += 1
                    for index in range(0, len(vec[0])-1):
                        cal[index] += vec[j][index]

            for index in range(0, len(vec[0])-1):
                a = float(cal[index])/float(cnt)
                cal[index] = float('%0.3f'%a)

            if cal != centroids[i]:
                clusterChanged = True
                centroids[i] = copy.deepcopy(cal)
            if clusterChanged == False:
                clusterAssment = clusterTemp
    return clusterAssment