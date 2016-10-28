import random
import numpy as np


def format_data(Filename):
    dataMatrix = []
    dataLabelMatrix = []
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
    return dataMatrix, dataLabelMatrix


def k_medoid(D, k):
    # D presents the data metric , k means k-clusters
    # D is np.darray type
    m = D.shape[0]
    medoids = []
    medoids_posi = []
    for i in range(0, k):
        medoids_posi.append(random.randint(0, m))
        medoids.append(D[medoids_posi])
    distance_to_medoid = {}
    for j in range(0, m):
        distance_to_medoid[j] =


data, label = format_data("DataSet1.txt")
k_medoid(data, 2)
