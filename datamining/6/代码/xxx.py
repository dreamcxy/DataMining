import pandas as pd 
import numpy as np
from pandas import Series,DataFrame
from sklearn.feature_extraction import DictVectorizer

data = {'state':[1,2,3,4,5],
        'year':[2000,2001,2002,2001,2002],
        'pop':[1.5,1.7,3.6,2.4,2.9]}
df = DataFrame(data,index=['one','two','three','four','five'],
               columns=['year','state','pop','debt'])
mkdict = lambda row: dict((col, row[col]) for col in cols)
cols = ['year','state']
x=df[cols].apply(mkdict, axis=1)
vec = DictVectorizer(sparse=False)
y=vec.fit_transform(x)
