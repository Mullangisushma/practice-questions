# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 06:11:34 2024

@author: sushm
"""

#autobiographical number

def bio(n):
    if n is None:
        return 0
    digit_count=[0]*10
    for i in n:
        i=int(i)
        digit_count[i]+=1
    for i in range(len(n)):
        if (int(n[i])!=digit_count[i]):
            return 0
    distinct_count=sum(1 for count in digit_count if count>0)
    return distinct_count
n=input()
result=bio(n)
print(result)