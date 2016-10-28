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
    cluster_matrix = [[]] * k  # last cluster matrix shape(k)
    cal_num = 0
    while cal_num <= 1000:
        for i in range(0, k):
            cluster_matrix[i] = []
        for i in range(0, m):
            distance = []
            for j in range(0, k):
                distance.append(linalg.norm(medoids(j) - D(i), 1)
            k_cluster = np.argmin(distance)  # return where the D(i) belongs
            # return cluster_matrix represents k-cluster
            cluster_matrix[k_cluster].append(D(i))
        new_medoids=[]
        for i in xrange(0, k):
            new_medoids.append(new_medoid(cluster_matrix[i]))
        cal_num = cal_num + 1
    return cluster_matrix

def new_medoid(k_cluster_vector):
    sum_distance=[]
    for i in range(0, len(k_cluster_vector)):
        distance=0
        for j in range(0, len(k_cluster_vector)):
            distance += np.linalg.norm(
                k_cluster_vector[i] - k_cluster_vector[j], 1)
        sum_distance.append(distance)
    new_medoid_pos=np.argmin(sum_distance)
    new_medoid=k_cluster_vector[new_medoid_pos]
    return new_medoid


# data, label = format_data("DataSet1.txt")
data=np.array([[1, 2, 3], [2, 2, 2], [3, 3, 3]])
k_medoid(data, 2)
