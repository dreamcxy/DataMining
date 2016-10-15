import nltk
import io
import os
import string
import stop_words
from math import log


def tokenize(filename):
    fileContent = io.open(filename, 'r', encoding='utf-8')
    segList = nltk.word_tokenize(fileContent.read())
    fileContent.close()
    result = []
    for seg in segList:
        seg = ''.join(seg.split())
        if seg != '' and seg != "\n" and seg != "\n\n":
            result.append(seg)
    return result


def clean_messy(fileline):
    identify = string.maketrans('', '')
    cleanLine = fileline.translate(identify, string.punctuation + string.digits)
    return cleanLine


def del_stopwords(word_instr):
    stopWords = set(stop_words.get_stop_words("english"))
    return [word for word in word_instr.lower().split() if word not in stopWords]


def calculate_tf(token_words, filename):
    result = {}
    TF = {}
    countAll = 0
    with io.open(filename, 'r', encoding='utf-8') as fileRead:
        allText = fileRead.read()
        for word in allText.split():
            if word not in result:
                result[word] = 0.0
            result[word] += 1.0
            countAll += 1.0
        for tokenWord in token_words:
            TF[tokenWord] = float(result[tokenWord] / countAll)
    return TF


dataDirNames = ['1. Active Learning',
                '2. Applications',
                '3. Bayesian Learning and Graphical Model',
                '4. Deep Learning',
                '5. Ensemble and Crowdsourcing',
                '6. Feature Learning',
                '7. Kernel Methods',
                '8. Online Learning',
                '9. Optimization',
                '10. Ranking',
                '11. Reinforcement Learning',
                '12. Supervised Learning',
                '13. Theory',
                '14. Unsupervised and Semi-Supervised Learning',
                '15. Others']

IDF = {}
TF = {}
TF_IDF = {}
TF7 = {}
allFiles = 581
for i in range(0, len(dataDirNames)):
    dirName = dataDirNames[i]
    os.chdir(dirName)
    if i != 6:
        for j in range(0, len(os.listdir(os.getcwd()))):
            with open('test.txt', 'a') as hacFileNew:
                with open(os.listdir(os.getcwd())[j], 'r') as hacFile:
                    for line in hacFile.readlines():
                        dealLine = ' '.join(del_stopwords(clean_messy(line)))
                        hacFileNew.write(dealLine)
            tokenWords = tokenize('test.txt')
            TF = calculate_tf(tokenWords, 'test.txt')
            for tokenWord in tokenWords:
                if tokenWord not in IDF:
                    IDF[tokenWord] = 0.0
                IDF[tokenWord] += 1.0
            os.remove('test.txt')
        with open("%dtf.txt" % i, 'a') as tf_file:
            tf_file.write(str(TF))
        os.chdir(os.path.abspath(os.path.join(os.path.dirname(os.getcwd()), os.pardir)))
        os.chdir('Lab1')
    else:
        for j in range(0, len(os.listdir(os.getcwd()))):
            with open('test.txt', 'a') as hacFileNew:
                with open(os.listdir(os.getcwd())[j], 'r') as hacFile:
                    for line in hacFile.readlines():
                        dealLine = ' '.join(del_stopwords(clean_messy(line)))
                        hacFileNew.write(dealLine)
            tokenWords = tokenize('test.txt')
            TF7 = calculate_tf(tokenWords, 'test.txt')
            for tokenWord in tokenWords:
                if tokenWord not in IDF:
                    IDF[tokenWord] = 0.0
                IDF[tokenWord] += 1.0
            os.remove('test.txt')
        with open("%dtf.txt" % i, 'a') as tf_file:
            tf_file.write(str(TF))
        os.chdir(os.path.abspath(os.path.join(os.path.dirname(os.getcwd()), os.pardir)))
        os.chdir('Lab1')
for word in IDF:
    IDF[word] = float(log(allFiles / IDF[word]))
print IDF
print len(IDF)

for word in TF7:
    TF_IDF[word] = TF7[word] * IDF[word]

print TF_IDF
