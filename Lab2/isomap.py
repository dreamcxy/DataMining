import numpy as np
from collections import defaultdict, deque

NEIGHBORNUMBER = 6


class Graph(object):
    """docstring for Graph"""

    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def addNode(self, value):
        self.nodes.add(value)

    def addEdge(self, startNode, endNode, distance):
        self.edges[startNode].append(endNode)
        self.edges[endNode].append(startNode)
        self.distances[(startNode, endNode)] = distance
        self.distances[(endNode, startNode)] = distance


def dijkstars(graph, initial):
    visited = {initial: 0}
    path = {}
    nodes = set(graph.nodes)
    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break
        nodes.remove(minNode)
        currentWeight = visited[minNode]
        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = minNode
    return visited, path


def shortestPath(graph, startNode, endNode):
    visited, paths = dijkstars(graph, startNode)
    fullPath = deque()
    end = paths[endNode]

    while end != startNode:
        fullPath.appendleft(end)
        end = paths[end]

    fullPath.appendleft(startNode)
    fullPath.append(endNode)

    return visited[endNode]
    # , list(fullPath)


def findFourNeighbor(dataMatrix, selfPosition):
    global NEIGHBORNUMBER
    distance = []
    for j in range(0, dataMatrix.shape[0]):
        distance.append(np.linalg.norm(
            dataMatrix[selfPosition] - dataMatrix[j]))
    distance = np.array(distance)
    neighborPosition = np.argsort(distance)[:NEIGHBORNUMBER + 1]
    return neighborPosition, distance[neighborPosition]


oldDataTrainMatrix = []
dataTrainDegree = []
with open('dataset1_training.txt', 'r') as dataFile:
    data = dataFile.readlines()
    for line in data:
        numbers = map(float, line.split(','))
        oldDataTrainMatrix.append(numbers[:-1])
        dataTrainDegree.append(numbers[-1])
oldDataTrainMatrix = np.array(oldDataTrainMatrix)  # shape(105*60)
dataTrainDegree = np.array(dataTrainDegree)  # shape(105,1)
nTrain = oldDataTrainMatrix.shape[0]
trainingGraph = Graph()
for i in range(0, nTrain):
    trainingGraph.addNode(i)
    neighborPosition, neighbordistance = findFourNeighbor(
        oldDataTrainMatrix, i)
    for j in range(1, len(neighborPosition)):
        trainingGraph.addEdge(i, neighborPosition[j], neighbordistance[j])
distanceMatrix = [[]] * nTrain
# for i in range(0, nTrain):
#     for j in range(0, nTrain):
#         if i == j:
#             distanceMatrix[i].append(0)
#         else:
#             if (i not in [83, 84, 85, 86, 87, 88]) and (j not in [83, 84, 85, 86, 87, 88]):
#                 distanceMatrix[i].append(shortestPath(trainingGraph, i, j))
#             else:
#                 distanceMatrix[i].append(np.linalg.norm(
#                     oldDataTrainMatrix[i] - oldDataTrainMatrix[j]))
for i in range(0, nTrain):
    for j in range(0, nTrain):
        if i == j:
            distanceMatrix[i].append(0)
        else:
            distanceMatrix[i].append(np.linalg.norm(
                oldDataTrainMatrix[i] - oldDataTrainMatrix[j]))

dTrain = np.array(distanceMatrix)[0].reshape(nTrain, nTrain)


# mds
k = 10  # low degree


def mds(d, n):
    D = pow(d, 2)
    Identity = np.eye(n)
    L = np.ones(n)
    J = Identity - (L * L.T) / n
    print J
    B = -(J * D * J) / 2
    bTrainEigValues, bTrainEigVectors = np.linalg.eig(B)
    kBTrainEigValues = np.argsort(bTrainEigValues)[-1:-(k + 1):-1]
    kBTrainEigVectors = bTrainEigVectors[:, kBTrainEigValues]

    valuesMatrix = np.diag(kBTrainEigValues)
    X = np.dot(kBTrainEigVectors, valuesMatrix)
    return X


lowTrain = mds(dTrain, nTrain)

oldDataTestMatrix = []
dataTestDegree = []
with open('dataset1_testing.txt', 'r') as dataTestFile:
    data = dataTestFile.readlines()
    for line in data:
        numbers = map(float, line.split(','))
        oldDataTestMatrix.append(numbers[:-1])
        dataTestDegree.append(numbers[-1])
oldDataTestMatrix = np.array(oldDataTestMatrix)  # shape(105*60)
dataTestDegree = np.array(dataTestDegree)  # shape(105,1)
nTest = oldDataTestMatrix.shape[0]
testGraph = Graph()
for i in range(0, nTest):
    testGraph.addNode(i)
    neighborPosition, neighbordistance = findFourNeighbor(
        oldDataTestMatrix, i)
    for j in range(1, len(neighborPosition)):
        testGraph.addEdge(i, neighborPosition[j], neighbordistance[j])
distanceMatrix = [[]] * nTest
# for i in range(0, nTest):
#     for j in range(0, nTest):
#         if i == j:
#             distanceMatrix[i].append(0)
#         else:
#             if (i not in [83, 84, 85, 86, 87, 88]) and (j not in [83, 84, 85, 86, 87, 88]):
#                 distanceMatrix[i].append(shortestPath(testGraph, i, j))
#             else:
#                 distanceMatrix[i].append(np.linalg.norm(
#                     oldDataTestMatrix[i] - oldDataTestMatrix[j]))
for i in range(0, nTest):
    for j in range(0, nTest):
        if i == j:
            distanceMatrix[i].append(0)
        else:
            distanceMatrix[i].append(np.linalg.norm(
                oldDataTestMatrix[i] - oldDataTestMatrix[j]))
dTest = np.array(distanceMatrix)[0].reshape(nTest, nTest)
lowTest = mds(dTest, nTest)
correct = 0
for testVector in lowTest:
    position = 0
    minDistance = []
    for trainVector in lowTrain:
        minDistance.append(np.linalg.norm(testVector - trainVector))
    minDistance = np.array(minDistance)
    minPosition = minDistance.argmin()
    newTestDegree = dataTrainDegree[minPosition]
    if newTestDegree == dataTestDegree[position]:
        correct = correct + 1
    position = position + 1

print correct / float(nTest)
