# -*- codeing = utf-8 -*-
# @TIME:2021/4/2016:37
# @File:词频加权统计.py
# @Software:PyCharm

# -*- coding: cp936 -*-
import jieba
import math
import jieba.posseg as pseg
import os
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import importlib,sys
importlib.reload(sys)
sys.path.append(r"C:\Users\jr\Desktop")
from numpy import *
fr = open('C://Users//jr//Desktop//西部.txt','r',encoding='UTF-8')
fr_list = fr.read()
dataList = fr_list.split('\n')
data = []
for oneline in dataList:
    data.append(" ".join(jieba.cut(oneline)))

#将得到的词语转换为词频矩阵
freWord = CountVectorizer()

#统计每个词语的tf-idf权值
transformer = TfidfTransformer()
#计算出tf-idf(第一个fit_transform),并将其转换为tf-idf矩阵(第二个fit_transformer)
tfidf = transformer.fit_transform(freWord.fit_transform(data))

#获取词袋模型中的所有词语
word = freWord.get_feature_names()

#得到权重
weight = tfidf.toarray()
tfidfDict = {}
for i in range(len(weight)):
    for j in range(len(word)):
        getWord = word[j]
        getValue = weight[i][j]
        if getValue != 0:
            if getWord in tfidfDict:
                tfidfDict[getWord] += int(getValue)
            else:
                tfidfDict.update({getWord: getValue})
sorted_tfidf = sorted(tfidfDict.items(),
                      key = lambda d:d[1],reverse = True)
print(freWord)
for i in sorted_tfidf:
    print (i[0] + '\t' + str(i[1]) +'\n')
