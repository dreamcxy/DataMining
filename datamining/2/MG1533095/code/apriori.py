from __future__ import division


L=[[]]                  #L的第k个元素频繁k项集
supportData={}          #频繁k项集及其对应的支持度
Lk=[]                   #每次生成的频繁k项集，每个元素是集合类型


def createDataSet():
    #创建交易记录数据库D
    #将二进制数据转换为十进制数据
    fr=open('assignment2-data.txt','r')
    DataSet=[]
    for line in fr:
        line=[int(i) for i in line.split()]
        tid=[]
        for index,item in enumerate(line):
            if item>0:
                tid.append(index+1)
        DataSet.append(tid)
    return DataSet[1:]


def canGen(Lk):
    #由频繁k项集Lk生成候选集Ck+1
    retList=[]
    lenLk=len(Lk)
    k=len(Lk[0])
    for i in range(lenLk):
        for j in range(i+1,lenLk):
            L1=list(Lk[i])[:k-1]
            L2=list(Lk[j])[:k-1]
            L1.sort()
            L2.sort()
            if(L1==L2):
                retList.append(Lk[i]|Lk[j])
    return retList


def pruning(Lk,Ck):
    #根据频繁k项集Lk，对候选集Ck+1进行剪枝
    for I in Ck:
        S=list(I)
        for i in range(len(S)):
            subset=S[:i]+S[i+1:]
            if set(subset) not in Lk:
                Ck.remove(I)
                break
    return Ck


class node:
    #所建立的hash树的每一个结点定义为一个结构体
    def __init__(self):
        self.candidate=[]         #每个结点包含的候选集
        self.num=0                #候选集在数据库中出现的次数，仅统计叶子结点
        self.branch={}            #每个结点的分支


def buildHashTree(root,level):
    #建立候选集Ck的哈希树
    if len(root.candidate)==1:
        return
    for can in root.candidate:
        hashKey=can[level]
        if hashKey not in root.branch:
            root.branch[hashKey]=node()
        root.branch[hashKey].candidate.append(can)
    for bran in root.branch.values():
        buildHashTree(bran,level+1)


def travelTree(tran,root):
    #递归地遍历哈希树
    if len(root.candidate)==1:
        if set(root.candidate[0]).issubset(set(tran)):
            root.num+=1
    else:
        for hashKey in root.branch:
            if hashKey in tran:
                travelTree(tran,root.branch[hashKey])


def travelDataSet(D,Ck):
    #用数据库中的每一条记录扫描哈希树
    TreeRoot=node()
    C=[]
    for can in Ck:
        c=list(can)
        c.sort()
        C.append(c)
    TreeRoot.candidate=C
    buildHashTree(TreeRoot,0)
    numTran=len(D)
    k=len(Ck[0])
    for i in range(numTran):
        d=list(D[i])
        d.sort()
        if(len(d)>=k):
            travelTree(d,TreeRoot)
    return TreeRoot


def supCount(root,numTran,minsup):
    #统计哈希树叶子结点上的值，求出频繁项集的支持度
    if len(root.candidate)==1:
        support=root.num/numTran
        if support>=minsup:
            supportData[frozenset(root.candidate[0])]=support
            Lk.append(frozenset(root.candidate[0]))
    else:
        for bran in root.branch.values():
            supCount(bran,numTran,minsup)


def apriori():
    #apriori算法
    global Lk
    minsup=0.144
    DataSet=createDataSet()
    D=list(map(set,DataSet))
    numTran=len(D)
    C1=[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11]]
    C1=list(map(frozenset,C1))
    Tree=travelDataSet(D,C1)
    supCount(Tree,numTran,minsup)
    if Lk:
        L.append(Lk)
    k=2
    while(len(L[k-1])>1):
        Ck=canGen(L[k-1])
        Ck=pruning(L[k-1],Ck)
        Lk=[]
        Tree=travelDataSet(D,Ck)
        supCount(Tree,numTran,minsup)
        if Lk:
            L.append(Lk)
        k+=1


def writeResult():
    #将程序的输出结果写出来
    apriori()
    fr=open('result.txt','w')
    result=[]
    for key in supportData:
        data=(list(key))
        data.sort()
        data.append(supportData[key])
        result.append(data)
    result.sort()
    for item in result:
        for i in item[:-1]:
            fr.write("%d "%i)
        fr.write("%.3f\n"%item[-1])
    fr.close()

writeResult()


