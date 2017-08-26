import nltk
import os
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sort import Sort
from Rotate import Rotate
from CreateFunction import CreateFunction
from JobSeq import JobSeq
msg="Hi"
while msg!="exit":
 msg=raw_input("");
 actiondict={"sort":"Sort()","rotate":"Rotate()", "jobsequence":"JobSeq()"}
 greet={'Hola':'Hola!!','Hey':'Hey What can I do for you','Who are you':'I am AlgoBot. I solve algorithms'}
 words=stopwords.words("english")
 if msg in greet.keys():
     print greet[msg]
 token=word_tokenize(msg)
 tok=[i.lower() for i in token if i not in words]
 comp=re.compile('\d+')
 num_list=comp.findall(msg)
 num_list=map(int,num_list)
 if "new function" in msg:
     num_list,k,a=msg.partition("new function")
     newfunc=CreateFunction()
     op=newfunc.create(a)
     print op
 for i in tok:
     if i in actiondict.keys():
         oper=eval(actiondict[i])
         res=oper.operation(list(num_list))
         num_list=res
         print res
