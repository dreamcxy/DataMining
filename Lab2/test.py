# import heapq


# class Vertex:

#     def __init__(self, node):
#         self.id = node
#         self.adjacent = {}

#     def __str__(self):
# return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

#     def add_neighbor(self, neighbor, weight=0):
#         self.adjacent[neighbor] = weight

#     def get_connections(self):
#         return self.adjacent.keys()

#     def get_id(self):
#         return self.id

#     def get_weight(self, neighbor):
#         return self.adjacent[neighbor]


# class Graph:

#     def __init__(self):
#         self.vert_dict = {}
#         self.num_vertices = 0

#     def __iter__(self):
#         return iter(self.vert_dict.values())

#     def add_vertex(self, node):
#         self.num_vertices = self.num_vertices + 1
#         new_vertex = Vertex(node)
#         self.vert_dict[node] = new_vertex
#         return new_vertex

#     def get_vertex(self, n):
#         if n in self.vert_dict:
#             return self.vert_dict[n]
#         else:
#             return None

#     def add_edge(self, frm, to, cost=0):
#         if frm not in self.vert_dict:
#             self.add_vertex(frm)
#         if to not in self.vert_dict:
#             self.add_vertex(to)

#         self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
#         self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

#     def get_vertices(self):
#         return self.vert_dict.keys()


# def dijkstars(graph, start, end):
#     start.set_distance(0)


# # graph = Graph()
# # for node in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
# #     graph.addNode(node)

# # graph.addEdge('A', 'B', 10)
# # graph.addEdge('A', 'C', 20)
# # graph.addEdge('B', 'D', 15)
# # graph.addEdge('C', 'D', 30)
# # graph.addEdge('B', 'E', 50)
# # graph.addEdge('D', 'E', 30)
# # graph.addEdge('E', 'F', 5)
# # graph.addEdge('F', 'G', 2)

# # print(shortestPath(graph, 'A', 'D'))  # output: (25, ['A', 'B', 'D'])
import numpy as np

t = np.ones(3)
print np.diag([2, 3])
d = 3
print float(d)
