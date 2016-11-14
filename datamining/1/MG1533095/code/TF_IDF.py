from __future__ import division
from os import listdir
from math import log
import jieba

NumberOfWord={}				#每个帖子中所含有的单词的个数
totalNumberOfDoc=0			#所有帖子的个数
WordBase=[]				#建立的单词字典
WordInDoc={}				#每个帖子中每个单词出现的次数
NumberOfDoc={}				#每个单词在所有帖子中出现的次数
NumberOfEveryClass=[0]*10	    	#每一个类中的帖子的数目
TF={}					#每个帖子中每个单词的词频
IDF={}					#每个帖子中每个单词的IDF值
TF_IDF={}				#每个帖子中每个单词的TF_IDF值
fr=open('Chinese-stop-words.txt','r',encoding = 'utf-8')
StopWordDict=fr.read().split()         	#应删除的词的词典
FileName=listdir('lily')        	#每个类所在文档的名字
NumberOfClass=len(FileName)             #类的数目

def data_process():  
    #统计相关数据
    global totalNumberOfDoc
    for i in range(NumberOfClass):
        fr=open('lily\\'+FileName[i],'r',encoding = 'utf-8')
        for Line in fr:
            WordInDoc[totalNumberOfDoc]={}
            NumberOfWord[totalNumberOfDoc]=0
            LineList=jieba.cut(Line)
            LineList=' '.join(LineList).split()
            LineList=[word for word in LineList if word not in StopWordDict]
            for word in LineList:
                NumberOfWord[totalNumberOfDoc]+=1
                WordInDoc[totalNumberOfDoc][word]=WordInDoc[totalNumberOfDoc].get(word,0)+1
                if word not in WordBase:    
                    WordBase.append(word)
            for word in WordInDoc[totalNumberOfDoc]:
                NumberOfDoc[word]=NumberOfDoc.get(word,0)+1
            NumberOfEveryClass[i]+=1
            totalNumberOfDoc+=1
            

def tfidf_calculate():  
    #计算tf、idf、tf-idf值
    global totalNumberOfDoc
    for k in range(totalNumberOfDoc):
        TF[k]={}
        IDF[k]={}
        TF_IDF[k]={}
        for word in WordInDoc[k]:
            TF[k][word]=WordInDoc[k][word]/NumberOfWord[k]
            IDF[k][word]=log(totalNumberOfDoc/NumberOfDoc[word],10)
            TF_IDF[k][word]=TF[k][word]*IDF[k][word]
            
def write_result():
    #将数据写入文件
    global totalNumberOfDoc
    j=0
    for i in range(NumberOfClass):
        fr=open('result\\'+FileName[i],'w')
        while j<sum(NumberOfEveryClass[0:(i+1)]):
            for index,word in enumerate(WordBase):
                if word in WordInDoc[j]:
                    s="<%d>:<%.4f>\t"%(index,TF_IDF[j][word])
                    fr.write(s)
            fr.write('\n')
            j+=1
        fr.close()

data_process()
tfidf_calculate()
write_result()         

                    

                    

                    

                    

                    

        
                    

                    

                    

                    

                    

                    

                    


































