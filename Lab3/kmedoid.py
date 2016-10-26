import numpy as np
import random
from sklearn.metrics.pairwise import pairwise_distances


def kMedoids(D, k, tmax=100):
    # determine dimensions of distance matrix D
    m, n = D.shape

    # randomly initialize an array of k medoid indices
    M = np.sort(np.random.choice(n, k))

    # create a copy of the array of medoid indices
    Mnew = np.copy(M)

    # initialize a dictionary to represent clusters
    C = {}
    for t in xrange(tmax):
        # determine clusters, i. e. arrays of data indices
        J = np.argmin(D[:, M], axis=1)
        for kappa in range(k):
            C[kappa] = np.where(J == kappa)[0]
        # update cluster medoids
        for kappa in range(k):
            J = np.mean(D[np.ix_(C[kappa], C[kappa])], axis=1)
            j = np.argmin(J)
            Mnew[kappa] = C[kappa][j]
        np.sort(Mnew)
        # check for convergence
        if np.array_equal(M, Mnew):
            break
        M = np.copy(Mnew)
    else:
        # final update of cluster memberships
        J = np.argmin(D[:, M], axis=1)
        for kappa in range(k):
            C[kappa] = np.where(J == kappa)[0]

    # return results
    return M, C

dataMatrix = []
dataLabelMatrix = []
Filename = 'DataSet1.txt'
with open(Filename, 'r') as dataFile:
    data = dataFile.readlines()
    for line in data:
        numbers = map(float, line.split(','))
        dataMatrix.append(numbers[:-1])
        if numbers[-1] == -1:
            dataLabelMatrix.append(0)
        else:
            dataLabelMatrix.append(numbers[-1])

dataMatrix = np.array(dataMatrix)
dataLabelMatrix = np.array(dataLabelMatrix)
D = pairwise_distances(dataMatrix, metric="euclidean")
M, C = kMedoids(D, 2)
# print('medois:')
# for point_idx in M:
#     print dataMatrix[point_idx]
print('')
print('clustering result:')

countError = 0
for label in C:
    for point_idx in C[label]:
        # print('label {0}: {1}'.format(label, dataMatrix[point_idx]))
        countError += abs(dataLabelMatrix[point_idx] - label)

print(dataMatrix.shape[0] - countError) / float(dataMatrix.shape[0])
