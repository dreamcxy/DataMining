import numpy
import copy
import kMeans


def distEnclud(vecA, vecB):
    dist = 0
    for i in range(0, len(vecA)-1):
        dist += pow(vecA[i] - vecB[i], 2)
    return dist


def minN(mat, n):
    for row in range(0, len(mat)):
        mat[row][row] = 10000

        for num in range(0, n):
            i = 0
            for j in range(1, len(mat)):
                if mat[row][i] > mat[row][j]:
                    i = j
            mat[row][i] = 10000

        for i in range(0,len(mat)):
            if mat[row][i] == 10000:
                if row == i:
                    mat[row][i] = n
                else:
                    mat[row][i] = -1
            else:
                mat[row][i] = 0


def spectral(R, k, n):
    W = []

    for i in range(0, len(R)):
        dist = []
        for j in range(0, len(R)):
            dist.append(0)
        W.append(dist)

    for i in range(0, len(R)):
        for j in range(i+1, len(R)):
            W[j][i] = W[i][j] = distEnclud(R[i], R[j])

    minN(W, 3)
    a, dist = numpy.linalg.eig(W)
    e = numpy.array(dist.T)
    idx = numpy.argsort(a)
    eigVec = []

    for i in range(0, k):
        eigVec.append(e[idx[i]])
    e = numpy.array(eigVec)
    e = e.T

    final = []

    for i in range(0, len(e)):
        tmp = []
        for j in range(0, k):
            a = e[i][j].real
            tmp.append(float('%0.3f'%a))
        tmp.append(0)
        final.append(tmp)

    return kMeans.kMeans(final, k, 1)
