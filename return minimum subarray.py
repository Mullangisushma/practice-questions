# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 06:41:32 2024

@author: sushm
"""

#return the minimum_subarray

def SubArray(arr,k):
    if arr is None or len(arr)<k:
        return None
    min=float('inf')
    min_arr=[]
    for i in range(len(arr)-k+1):
        subarray=arr[i:i+k]
        sum_subarray=sum(subarray)
        if(sum_subarray<min):
            min=sum_subarray
            min_array=subarray
    return min_array
    
    
arr=list(map(int,input().split()))
k=int(input())
res=SubArray(arr,k)
print(res)