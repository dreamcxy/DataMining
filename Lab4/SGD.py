from numpy import *
import random


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


def in_random_order(data_matrix):
    indexes = [i for i, _ in enumerate(data_matrix)]
    random.shuffle(indexes)
    for i in indexes:
        yield data_matrix[i]


def upgrade_theta(theta_0, alpha, gradient_function):
    return [theta_0_i - upgrade_theta_i for theta_0_i, upgrade_theta_i in
            zip(theta_0, alpha * gradient_function(theta_0))]


def log_likelihood(theta, lamda, data_matrix, data_label):
    m, n = data_matrix.shape
    return (sum(log(1 + math.exp(-data_label[i]*dot(theta, data_matrix[i].T))) for i in range(0, m-1))/m) + lamda * linalg.norm(theta, 1)

def ridge_regression(theta, lamda, data_matrix, data_label):
    m, n = data_matrix.shape
    return (sum((data_label[i] - dot(theta, data_matrix[i].T))) for i in range(0, m -1)/m) + lamda* pow(linalg.norm(theta, 2),2)



def minimize_stochastic(file_name, target_function, gradient_function, iterations, lamda, theta_0, alpha_0=0.1):
    data_matrix, data_label = load_data(file_name)
    m, n = data_matrix.shape
    theta = theta_0
    alpha = alpha_0
    min_theta, min_value = None, float("inf")
    iterations_with_no_improvement = 0

    while iterations_with_no_improvement < iterations:
        value = (sum(log(1 + exp(-data_label * theta * data_matrix))) / n) + lamda * linalg.norm(theta, 1)
        if value < min_value:
            min_theta, min_value = theta, value
            iterations_with_no_improvement = 0
            alpha = alpha_0
        else:
            iterations_with_no_improvement += 1
            alpha *= 0.9

        for x_i, y_i in in_random_order(data_matrix):
            gradient_i = gradient_function()
    return min_theta
