# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 18:54:56 2024

@author: sushm
"""

"""
The function accepts two positive integers ‘r’ and ‘unit’ and a positive integer array ‘arr’ of size ‘n’ as its argument ‘r’ represents the number of rats present in an area, ‘unit’ is the amount of food each rat consumes and each ith element of array ‘arr’ represents the amount of food present in ‘i+1’ house number, where 0 <= i

Note:

Return -1 if the array is null
Return 0 if the total amount of food from all houses is not sufficient for all the rats.
Computed values lie within the integer range.
Example:

Input:

r: 7
unit: 2
n: 8
arr: 2 8 3 5 7 4 1 2
"""
def calculate(r,unit,n,arr):
    if arr is None:
        return -1
    totalfoodrequired=r*unit
    foodtillnow=0
    housestillnow=0
    for i in range(len(arr)):
        foodtillnow+=arr[i]
        housestillnow+=1
        if(foodtillnow>totalfoodrequired):
            break
    if(foodtillnow<totalfoodrequired):
        return 0
    return housestillnow
r=int(input())
unit=int(input()) 
n=int(input()) 
arr=list(map(int,input().split()))   
result=calculate(r,unit,n,arr)
print(result)   
    