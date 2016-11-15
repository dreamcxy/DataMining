# import math

# from numpy import *


# def load_data(file_name):
#     data_matrix = []
#     data_label = []
#     with open(file_name, 'r') as dataFile:
#         data_lines = dataFile.readlines()
#         for line in data_lines:
#             data = map(float, line.split(','))
#             data_matrix.append(data[:-1])
#             data_label.append(data[-1])
#     return array(data_matrix), array(data_label)


# #
# # def partial_difference_quotient(f, v, i, h):
# #     w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]
# #     return (f(w) - f(v)) / h
# #
# #
# # def estimate_gradient(f, v, h=0.00001):
# #     return [partial_difference_quotient(f, v, i, h)
# #             for i, _ in enumerate(v)]

# def calculate_norm_sub_gradient(theta, h=0.00001):
#     return (linalg.norm(theta + h) - linalg.norm(theta)) / h


# def upgrade_theta(theta_0, alpha, gradient_function):
#     return [theta_0_i - upgrade_theta_i for theta_0_i, upgrade_theta_i in
#             zip(theta_0, alpha * gradient_function(theta_0))]


# def log_likelihood(theta, lamda, data_matrix, data_label):
#     m, n = data_matrix.shape
#     return (sum(log(1 + math.exp(-data_label[i] * dot(theta, data_matrix[i].T))) for i in
#                 range(0, m - 1)) / m) + lamda * linalg.norm(theta, 1)
# data_matrix, data_label = load_data('test.txt')
# m, n = data_matrix.shape
# theta = ones(n)
# print log_likelihood(theta, 0, data_matrix, data_label)
# print sum(data_matrix[2])
# print data_matrix[2]
# count = 0
# for i in range(0,data_matrix[2].shape[0]):
#     count  += data_matrix[2][i]
# print count

from math import e
print 2.7*2.7

