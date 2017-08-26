import os
import operator
import collections
class JobSeq:
    def __init__(self):
        pass
    def operation(self,dicti):
     if(len(dicti)%2 !=0):
            print "Wrong Input to be processed"
     else:
        profit=[]
        time=[]
        for i in dicti[0:len(dicti)/2]:
            profit.append(i)
        for i in dicti[len(dicti)/2:]:
            time.append(i)
        slot=[]
        res=[]
        d=dict(zip(profit,time))
        for i in range(len(time)):
            slot.append(False);
        m=collections.OrderedDict(sorted(d.items(),reverse=True))
        k =list(m.keys())
        for l in k:
            i=m[l]
            while(i!=0):
                if(slot[i]==False):
                    slot[i]=True
                    res.append(l)
                    break
                i-=1
        return res
