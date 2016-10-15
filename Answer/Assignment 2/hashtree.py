class node:

    def __init__(self):
        self.candidate = []
        self.num = 0
        self.branch = {}


def buildHashTree(root, level):
    if len(root.candidate) == 1:
        return
    for can in root.candidate:
        hashKey = can[level]
        if hashKey not in root.branch:
            root.branch[hashKey] = node()
        root.branch[hashKey].candidate.append(can)
    for bran in root.branch.values():
        buildHashTree(bran, level + 1)


def travelTree(tran, root):
    if len(root.candidate) == 1:
        if set(root.candidate[0]).issubset(set(tran)):
            root.num += 1
    else:
        for hashKey in root.branch:
            if hashKey in tran:
                travelTree(tran, root.branch[hashKey])


def travelDataSet(D, Ck):
    TreeRoot = node()
    C = []
    for can in Ck:
        c = list(can)
        c.sort()
        C.append(c)
    TreeRoot.candidate = C
    buildHashTree(TreeRoot, 0)
    numTran = len(D)
    k = len(Ck[0])
    for i in range(numTran):
        d = list(D[i])
        d.sort()
        if(len(d) >= k):
            travelTree(d, TreeRoot)
    return TreeRoot


def supCount(root, numTran, minsup):
    supportData = {}
    if len(root.candidate) == 1:
        support = root.num / numTran
        if support >= minsup:
            supportData[frozenset(root.candidate[0])] = support
            Lk.append(frozenset(root.candidate[0]))
    else:
        for bran in root.branch.values():
            supCount(bran, numTran, minsup)
