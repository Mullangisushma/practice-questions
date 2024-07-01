# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 05:48:28 2024

@author: sushm
"""
#weights on mars and earth
def unique_weights_on_mars(m,n,common_stones):
    mars_weight=list(range(1,(m+1)))
    earth_weight=common_stones
    mars_set=set(mars_weight)
    earth_set=set(earth_weight)
    unique_mars_weight=list(mars_set-earth_set)
    total_stones=0
    total_weight=0
    unique_mars_weight.sort()
    for weight in unique_mars_weight:
        if total_weight+weight<=m:
            total_weight+=weight
            total_stones+=1
        else:
            break
    return total_stones
m=int(input())
n=int(input()) 
common_stones=list(map(int,input().split())) 
res=unique_weights_on_mars(m,n,common_stones)      
print(res)