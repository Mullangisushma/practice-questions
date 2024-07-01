# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 19:20:18 2024

@author: sushm
"""

#cars fine on particular date

date=int(input())
n=int(input())
if(n==0):
    print(-1)
else:
    cars=list(map(int,input().split()))
    fine=0
    if(date%2==0):
        for i in cars:
            if i%2!=0: 
                fine+=250
    else:
        for i in cars:
            if i%2==0:
                fine+=250
print(fine)
    