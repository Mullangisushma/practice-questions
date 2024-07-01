# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 07:20:07 2024

@author: sushm
"""

#count of distinct elements

def distinct(arr,n):
    count=0
    for i in range(n):
        flag=0
        for j in range(i+1,n):
            if(arr[i]==arr[j]):
                flag=1
                break
        if(flag==0):
            count+=1
    return count
n=int(input())
arr=list(map(int,input().split()))
count=distinct(arr,n)
print(count)