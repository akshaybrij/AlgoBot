import os
from Sort import *;
from nltk.tokenize import word_tokenize
import re
funcdict={'sort':'Sort()'}
class CreateFunction:
    def __init__(self):
        pass
    def create(self,procstr):
        tokens=word_tokenize(procstr)
        dig=re.compile('\d+')
        dig=dig.findall(procstr)
        return dig
        
