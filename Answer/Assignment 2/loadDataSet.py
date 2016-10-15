import io
import hashtree

dataSet = []
with open("assignment2-data.txt", 'r') as fr:
    for line in fr:
        line = line.strip('\xef\xbb\xbf')
        line = line.strip('\n')
        dataSet.append(line)

length = len(dataSet)

for i in range(length):
    dataSet[i] = dataSet[i].split(" ")

for j in range(length):
    for k in range(11):
        if dataSet[j][k] == '1':
            dataSet[j][k] = k + 1
    dataSet[j] = [item for item in dataSet[j] if item != '0']

dataSet.pop(0)


def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return map(frozenset, C1)


def aprioriGen(Lk, k):
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            L1 = list(Lk[i])[:k - 2]
            L2 = list(Lk[j])[:k - 2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(Lk[i] | Lk[j])
    return retList


def pruning(Lk, Ck):
    for I in Ck:
        S = list(I)
        for i in range(len(S)):
            subset = S[:i] + S[i + 1:]
            if set(subset) not in Lk:
                Ck.remove(I)
                break
    return Ck


def apriori():
    Lk = []
    L = [[]]
    D = list(map(set, dataSet))
    numTran = len(D)
    C1 = createC1(dataSet)
    Tree = hashtree.travelDataSet(D, C1)
    hashtree.supCount(Tree, numTran, minsup=0.144)
    if Lk:
        L.append(Lk)
    k = 2
    while(len(L[k - 2]) > 0):
        Ck = aprioriGen(L[k - 2])
        Ck = pruning(L[k - 1], Ck)
        Lk = []
        Tree = hashtree.travelDataSet(D, Ck)
        hashtree.supCount(Tree, numTran, minsup=0.144)
        if Lk:
            L.append(Lk)
        k += 1


def writeResult():
    apriori()
    fr = open('result.txt', 'w')
    result = []
    for key in supportData:
        data = (list(key))
        data.sort()
        data.append(supportData[key])
        result.append(data)
    result.sort()
    for item in result:
        for i in item[:-1]:
            fr.write("%d " % i)
        fr.write("%.3f\n" % item[-1])
    fr.close()

writeResult()
