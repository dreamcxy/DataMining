# 第一步：数据准备，生成图的邻接矩阵；
# 第二步：归一化普拉斯矩阵；
# 第三步：生成最小的k个特征值和对应的特征向量；
# 第四步：将特征向量kmeans聚类(少量的特征向量)；


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

