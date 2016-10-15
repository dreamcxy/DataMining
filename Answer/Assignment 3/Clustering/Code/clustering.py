import nmf
import kMeans
import numpy
import spectral
import calculate

mDataSet = []
gDataSet = []
categoryG = []
categoryM = []

with open('german.txt', 'r') as gFr:
    for line in gFr:
        a = line.split(',')
        b = []
        for item in a:
            b.append(float(item))
        if b[-1] == -1:
            categoryG.append(0)
        else:
            categoryG.append(1)
        gDataSet.append(b)
gFr.close()

with open('mnist.txt', 'r') as mFr:
    for line in mFr:
        a = line.split(',')
        b = []
        for item in a:
            b.append(float(item))
        categoryM.append(b[-1])
        mDataSet.append(b)
mFr.close()


calculate.calculate(kMeans.kMeans(gDataSet, 2), categoryG, 2)

calculate.calculate(kMeans.kMeans(mDataSet, 10), categoryM, 10)

calculate.calculate(nmf.NMF(gDataSet, 2), categoryG, 2)

calculate.calculate(nmf.NMF(mDataSet, 10), categoryG, 10)

calculate.calculate(spectral.spectral(gDataSet, 2, 3), categoryG, 2)

calculate.calculate(spectral.spectral(gDataSet, 2, 6), categoryG, 2)

calculate.calculate(spectral.spectral(gDataSet, 2, 9), categoryG, 2)

calculate.calculate(spectral.spectral(mDataSet, 10, 3), categoryM, 10)

calculate.calculate(spectral.spectral(mDataSet, 10, 6), categoryM, 10)

calculate.calculate(spectral.spectral(mDataSet, 10, 9), categoryM, 10)

