# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 20:19:37 2024

@author: sushm
"""
def check(s,n):
    if(n<4):
        return 0
    if(s[0].isdigit()):
        return 0
    cap=0
    num=0
    for i in s:
        if(i==' ' or i=='/'):
            return 0
        if(i>='A' and i<='Z'):
            cap+=1
        if(i.isdigit()):
            num+=1
    if(cap>0 and num>0):
        return 1
    else:
        return 0
    
    
n=int(input())
s=input()
result=check(s,n)
print(result)