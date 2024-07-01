# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 20:08:54 2024

@author: sushm
"""

arr=list(map(int,input().split()))
even=[]
odd=[]
for i in range(0,len(arr)):
    if(i%2==0):
        even.append(arr[i])
    else:
        odd.append(arr[i])
even.sort()
odd.sort()
sum=even[-2]+odd[-2]
print(sum)