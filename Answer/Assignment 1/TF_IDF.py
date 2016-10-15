from os import listdir
from math import log
import jieba
import io

sum_of_word = {}
FILE_NUM = 0
word_list = []
word_of_single_file = {}
word_of_all_files = {}
NumberOfEveryClass = [0] * 10
TF = {}
IDF = {}
TF_IDF = {}
fr = io.open('Chinese-stop-words.txt', 'r', encoding='utf-8')
stop_word_list = fr.read().split()
file_names = listdir('lily')
num_of_files = len(file_names)


def data_process():
    global FILE_NUM
    for i in range(num_of_files):
        fr = io.open('lily\\' + file_names[i], 'r', encoding='utf-8')
        for Line in fr:
            word_of_single_file[FILE_NUM] = {}
            sum_of_word[FILE_NUM] = 0
            LineList = jieba.cut(Line)
            LineList = ' '.join(LineList).split()
            LineList = [
                word for word in LineList if word not in stop_word_list]
            for word in LineList:
                sum_of_word[FILE_NUM] += 1
                word_of_single_file[FILE_NUM][
                    word] = word_of_single_file[FILE_NUM].get(word, 0) + 1
                if word not in word_list:
                    word_list.append(word)
            for word in word_of_single_file[FILE_NUM]:
                word_of_all_files[word] = word_of_all_files.get(word, 0) + 1
            NumberOfEveryClass[i] += 1
            FILE_NUM += 1


def tfidf_calculate():
    # 计算tf、idf、tf-idf值
    global FILE_NUM
    for k in range(FILE_NUM):
        TF[k] = {}
        IDF[k] = {}
        TF_IDF[k] = {}
        for word in word_of_single_file[k]:
            TF[k][word] = word_of_single_file[k][word] / sum_of_word[k]
            IDF[k][word] = log(FILE_NUM / word_of_all_files[word], 10)
            TF_IDF[k][word] = TF[k][word] * IDF[k][word]


def write_result():
    # 将数据写入文件
    global FILE_NUM
    j = 0
    for i in range(num_of_files):
        fr = io.open('result\\' + file_names[i], 'w')
        while j < sum(NumberOfEveryClass[0:(i + 1)]):
            for index, word in enumerate(word_list):
                if word in word_of_single_file[j]:
                    s = "<%d>:<%.4f>\t" % (index, TF_IDF[j][word])
                    fr.write(s)
            fr.write('\n')
            j += 1
        fr.close()

data_process()
tfidf_calculate()
write_result()
