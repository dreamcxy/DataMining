import numpy

def match(vec, r, k):
    if k == 2:
        _0Cnt = 0
        _1Cnt = 0
        for i in range(0, 2):
            if vec[i] == r[i]:
                _1Cnt += 1
            else:
                _0Cnt += 1
        if _0Cnt < _1Cnt:
            return [0, 1]
        else:
            return [1, 0]
    else:
        tempList = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        for i in range(0, 10):
            for i in range(0, 10):
                b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                for j in range(0, 10000):
                    b[vec[j]] += 1
                while True:
                    max = 0
                    for j in range(0, 10):
                        if b[max] < b[j]:
                            max = j
                        b[max] = -1
                        if tempList[i] == -1:
                            tempList[i] = j
                            break
        return tempList


def pij_matrix(vec, r, index_array):
    matrix = []
    tempList = []
    tmg = []
    for i in range(0, len(index_array)):
        b = []
        for j in range(0, len(index_array)):
            b.append(0)
        b.append(0)
        matrix.append(b)
        tempList.append(0)
        tmg.append(0)

    counter = 0
    for i in range(0, len(index_array)):   #统计mij，mi = matrix[][-1]
        for j in range(0, len(vec)):
            if vec[j] == i:
                counter += 1
                matrix[index_array[i]][-1] += 1
                matrix[index_array[i]][r[j]] += 1

    aver_p = 0
    aver_g = 0
    for i in range(0, len(index_array)):
        print i
        print matrix[i]
        tempList[index_array[i]] = matrix[i][i]

        tmp_g = 0
        for j in range(0, len(index_array)):
            tmp_g += pow(float(matrix[i][j])/float(matrix[i][-1]), 2)
        tmg[index_array[i]] = (1-tmp_g)*float(matrix[i][-1])
        aver_g += tmg[index_array[i]]
        aver_p += tempList[index_array[i]]
    aver_p = aver_p/float(len(r))
    aver_g = aver_g/float(len(r))


def calculate(vec, r, k):
    pij_matrix(vec, r, match(vec, r, k))