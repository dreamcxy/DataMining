def load_data(file_name): 导入数据
def calculate_norm_sub_gradient(theta, h=0.00001): 计算norm的次导数
def gradient_log_likelihood(data_matrix, data_label, lamda, theta, m): 计算log_likelihood的导数
def gradient_ridge_regression(data_matrix, data_label, lamda, theta, m): 计算ridge_regression的导数
def upgrade_theta(theta, alpha, gradient_function, data_matrix, data_label, lamda, m): 更新 theta的值
def minimize_stochastic(file_name, target_function, gradient_function, iterations, lamda=1, alpha_0=0.1): 进行迭代
def calculate_probability(theta, x): 计算theta情况下向量属于label的概率
def calculate_error(data_matrix, data_label, theta, m):计算正确率

只需要更新file_name_train, file_name_test就可以得到结果
画图利用excel，对result.xlsx中的数据进行绘图即可