import random

from numpy import *


def load_data(file_name):
    data_matrix = []
    data_label = []
    with open(file_name, 'r') as dataFile:
        data_lines = dataFile.readlines()
        for line in data_lines:
            data = map(float, line.split(','))
            data_matrix.append(data[:-1])
            data_label.append(data[-1])
    return array(data_matrix), array(data_label)


def calculate_norm_sub_gradient(theta, h=0.00001):
    return (linalg.norm(theta + h) - linalg.norm(theta)) / h


def gradient_log_likelihood(data_matrix, data_label, lamda, theta, m):
    i = random.randint(0, m - 1)
    return (lamda * calculate_norm_sub_gradient(theta) + (-data_label[i] + sum(data_matrix[i]))) / (
        m * (1 + exp(-data_label[i] * dot(theta, data_matrix[i].T))))


def gradient_ridge_regression(data_matrix, data_label, lamda, theta, m):
    i = random.randint(0, m - 1)
    return (2 * sum(data_matrix[i]) * (dot(theta, data_matrix[i].T) - data_label[i]) + 2 * lamda * linalg.norm(theta,
                                                                                                               1)) / m


def upgrade_theta(theta_0, alpha, gradient_function, data_matrix, data_label, lamda, theta, m):
    return theta_0 - alpha * gradient_function(data_matrix, data_label, lamda, theta, m)


def log_likelihood(theta, lamda, data_matrix, data_label):
    m, n = data_matrix.shape
    return (sum(log(1 + math.exp(-data_label[i] * dot(theta, data_matrix[i].T))) for i in
                range(0, m - 1)) / m) + lamda * linalg.norm(theta, 1)


def ridge_regression(theta, lamda, data_matrix, data_label):
    m, n = data_matrix.shape
    return ((sum((data_label[i] - dot(theta, data_matrix[i].T))) for i in range(0, m - 1)) / m) + lamda * pow(
        linalg.norm(theta, 2), 2)


def minimize_stochastic(file_name, target_function, gradient_function, iterations, lamda=0, alpha_0=0.1):
    data_matrix, data_label = load_data(file_name)
    m, n = data_matrix.shape
    theta_0 = ones(n)
    theta = theta_0
    alpha = alpha_0
    min_theta, min_value = None, float("inf")
    iterations_num = 0
    while iterations_num < iterations:
        value = target_function(theta, lamda, data_matrix, data_label)
        print value
        if value < min_value:
            min_theta, min_value = theta, value
            alpha = alpha_0
        else:
            iterations_num += 1
            alpha *= 0.9
        theta = upgrade_theta(theta, alpha, gradient_function, data_matrix, data_label, lamda, theta, m)
    return min_theta


print minimize_stochastic('training1.txt', log_likelihood, gradient_log_likelihood, 100)
