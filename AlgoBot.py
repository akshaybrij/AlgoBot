import nltk
import os
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sort import Sort
from Rotate import Rotate
msg="Hi"
while msg!="exit":
 msg=raw_input("");
 actiondict={"sort":"Sort()","rotate":"Rotate()"}
 greet={'Hola':'Hola!!','Hey':'Hey What can I do for you','Who are you':'I am AlgoBot. I solve algorithms'}
 words=stopwords.words("english")
 if msg in greet.keys():
     print greet[msg]
 token=word_tokenize(msg)
 tok=[i.lower() for i in token if i not in words]
 comp=re.compile('\d+')
 num_list=comp.findall(msg)
 num_list=map(int,num_list)
 for i in tok:
     if i in actiondict.keys():
         oper=eval(actiondict[i])
         res=oper.operation(list(num_list))
         num_list=res
         print res
