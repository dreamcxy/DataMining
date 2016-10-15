import numpy


def matrixFac(R, P, Q, K, steps=500, alpha=0.0002, beta=0.02):
    Q = Q.T
    for step in xrange(steps):
        for i in xrange(len(R)):
            for j in xrange(len(R[i])):
                if R[i][j] > 0:
                    eij = R[i][j] - numpy.dot(P[i,:],Q[:,j])
                    for k in xrange(K):
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])
        eR = numpy.dot(P, Q)
        e = 0
        for i in xrange(len(R)):
            for j in xrange(len(R[i])):
                if R[i][j] > 0:
                    e += pow(R[i][j] - numpy.dot(P[i, :], Q[:, j]), 2)
                    for k in xrange(K):
                        e += (beta/2) * (pow(P[i][k], 2) + pow(Q[k][j], 2))
        if e < 0.001:
            break
    return P, Q.T

def NMF(vec, k):
    nmfAssment = []
    N = len(vec)
    M = len(vec[0])
    K = 2

    P = numpy.random.rand(N, 2)
    Q = numpy.random.rand(M, 2)

    nP, nQ = matrixFac(vec, P, Q, 2)
    NP = numpy.array(nP)

    i = 0
    while i < len(vec):
        j = 0
        k = 1
        while k <= len(NP[0])-1:
            if NP[i][j] > NP[i][k]:
                j = k
            k += 1
        nmfAssment.append(len(NP[0])-1-j)
        i += 1
    return nmfAssment