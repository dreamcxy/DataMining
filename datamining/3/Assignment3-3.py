import numpy as np

#************************初始化**************************
which = 1
#0:数据集1
#1:数据集2
data_number_lst = [1000,10000]
class_number_lst = [2,10]
abbr_number_lst = [25,785]
file_lst = ['german.txt','mnist.txt']

data_number = data_number_lst[which]
class_number = class_number_lst[which]
abbr_number = abbr_number_lst[which]
file = file_lst[which]
para_n = 9

data = []

dis_matrix = np.zeros((data_number,data_number))
W_matrix = np.zeros((data_number,data_number))
D_matrix = np.zeros((data_number,data_number))
L_matrix = np.zeros((data_number,data_number))
LD_matrix = np.zeros((data_number,data_number))

#************************函数**************************
def distance(line_1,line_2):
    sum = 0
    for i in range(abbr_number - 1):
        sum += (line_1[i] - line_2[i]) ** 2
    return sum

#************************主程序**************************
print('……读取文件数据……')
file = open(file, 'r')
for line in file:
    ele = []
    temp = line.rstrip('\n').split(',')
    for i in range(abbr_number):
        ele.append(float(temp[i]))
    data.append(ele)
file.close()

print('……计算每个点之间的距离……')
for i in range(data_number):
    print('dis',i)
    dis_matrix[i][i] = float('inf')
    for j in range(i + 1,data_number):
        dis_matrix[i][j] = dis_matrix[j][i] = distance(data[i],data[j])

print('……计算W矩阵……')
for i in range(data_number):
    print('w',i)
    mins = []
    for j in range(para_n):
        mins.append([dis_matrix[i][j],j])
    mins.sort()
    for j in range(para_n,data_number):
        if dis_matrix[i][j] < mins[para_n - 1][0]:
            mins[para_n - 1][0] = dis_matrix[i][j]
            mins[para_n - 1][1] = j
            mins.sort()
    for j in range(para_n):
        W_matrix[i][mins[j][1]] = W_matrix[mins[j][1]][i] = 1

print('……计算D矩阵……')
temp = W_matrix.sum(axis = 0)
for i in range(data_number):
    D_matrix[i][i] = temp[i]

print('……计算L矩阵……')
L_matrix = D_matrix - W_matrix

print('……计算特征值和特征向量……')
LD_matrix = np.dot(np.linalg.inv(D_matrix),L_matrix)
values,valuevector = np.linalg.eig(LD_matrix)

print('……特征值和特征向量排序……')
values_vector = []
for i in range(data_number):
    values_vector.append([values[i],valuevector[:,i]])
values_vector.sort(key=lambda x : x[0])

print('……计算低维表示……')
low_data = []
for i in range(data_number):
    a_low_data = []
    for j in range(1,class_number + 1):
        a_low_data.append(values_vector[j][1][i])
    low_data.append(a_low_data)

print('……写入中间文件……')
file = open('median.txt', 'w')
for i in range(data_number):
    string = ''
    for j in range(class_number):
        string += str(low_data[i][j]) + ','
    string += str(data[i][abbr_number - 1])
    file.write(string + '\n')
file.close()





















print('程序结束！')
