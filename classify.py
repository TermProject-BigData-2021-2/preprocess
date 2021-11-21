import os
import pandas as pd
import re
import numpy

m = ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP','INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']
postdata = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

# Read file
def getFile():
    fileName = './mbti_1.csv'
    filedata = pd.read_csv(fileName)
    data = list(zip(filedata.type, filedata.posts))
    return data
d = getFile()

# Classify MBTI Types, 3-dimension array
for (t,p) in d:
    loc = m.index(t)
    postdata[loc].append(p)

# Join Total posts of each MBTI Types, 2-dimension array
tempdata = []
for item in postdata:
    tempdata.append('|||'.join(item))
# print(len(tempdata))

newdata = []
for text in tempdata:
    # URL
    text = re.sub('(http|ftp|https|uhttp|$uhttp)://(?:[-\w.]|(?=:%[\da-fA-F]{2}))+', ' ', text)
    text = re.sub('http://([\d\w\./])+/[\d\w\./]+ ', ' ', text)
    text = re.sub('http://([\d\w\./])+/[\d\w\./]+.', ' ', text)
    text = re.sub('http : \*\*([\d;])+;TOOLONG', ' ', text)
    # html tags
    text = re.sub(r'<[^>]+>', ' ', text)
    # email
    text = re.sub('([a-z0-9_.+-]+@[a-z0-9-]+\.[a-z0-9-.]+)', ' ', text)
    # image formats
    text = re.sub('[\d\w\./]+.(jpg|jpeg|png|pdf|gif|bmp)', ' ', text)
    # minimize blank spaces
    text = re.sub(' +', ' ', text)
    # split to list
    text_split = text.split('|||')
    # 
    # Delete blank entry
    t = list(map(lambda s: s.strip(), text_split))
    t = list(filter(None, t))
    # print(len(t))
    newdata.append(t)

# WriteFile
# data = {
#     'ISTJ': [newdata[0]],
#     'ISFJ': [newdata[1]],
#     'INFJ': [newdata[2]],
#     'INTJ': [newdata[3]],
#     'ISTP': [newdata[4]],
#     'ISFP': [newdata[5]],
#     'INFP': [newdata[6]],
#     'INTP': [newdata[7]],
#     'ESTP': [newdata[8]],
#     'ESFP': [newdata[9]],
#     'ENFP': [newdata[10]],
#     'ENTP': [newdata[11]],
#     'ESTJ': [newdata[12]],
#     'ESFJ': [newdata[13]],
#     'ENFJ': [newdata[14]],
#     'ENTJ': [newdata[15]]
# }
data = {
    'ISTJ': newdata[0],
    'ISFJ': newdata[1],
    'INFJ': newdata[2],
    'INTJ': newdata[3],
    'ISTP': newdata[4],
    'ISFP': newdata[5],
    'INFP': newdata[6],
    'INTP': newdata[7],
    'ESTP': newdata[8],
    'ESFP': newdata[9],
    'ENFP': newdata[10],
    'ENTP': newdata[11],
    'ESTJ': newdata[12],
    'ESFJ': newdata[13],
    'ENFJ': newdata[14],
    'ENTJ': newdata[15]
}

dd = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in data.items() ]))
# data_df = pd.DataFrame.from_dict(data)
# data_fin = data_df.transpose()
dd.to_csv('./data-clean2.csv', sep=',')
