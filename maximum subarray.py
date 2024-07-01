# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 19:07:33 2024

@author: sushm
"""

#maximum subarray problem

n=int(input())
arr=list(map(int,input().split()))
max_sum=arr[0]
present_sum=arr[0]
for i in arr[1:]:
    present_sum=max(present_sum,present_sum+i)
    max_sum=max(max_sum,present_sum)
print(max_sum)