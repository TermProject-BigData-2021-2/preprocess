import os
import pandas as pd
import re
import numpy

smiley = [';)', ':)', ':-)', '|-)', '|-D', ' :->', '\'-)', ';->', ':*)', ';-)', 'B-)', '8-]', ':-]', 'xD', ':^D', '^^']
unhappy = [':(', ':-(' , ';(', ':\'(', ':-c', ':-C', ':-<', ':-X', ':-x', ':-@', ':-&', ':-r', ':-V', ':@', '\-o', ':-I']
another = [':O', ':-o', '8-O', '8-|', ':-T', ':/', ':P', ':-p', ':3', '8-|', ':-\\', ':~/']
imoticon = smiley + unhappy + another
print(imoticon)
           

           



# Read file
def getFile():
    fileName = './mbti_1.csv'
    filedata = pd.read_csv(fileName)
    data = list(zip(filedata.type, filedata.posts))
    return data
d = getFile()

