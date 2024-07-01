# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 20:44:34 2024

@author: sushm
"""
#operationsBinaryString



str=input()
if str is None:
    print(-1)
result=int(str[0])
for i in range(1,len(str),2):
    operator=str[i]
    operand=int(str[i+1])
    if(operator=='A'):
        result=result and operand   #and operation
    elif(operator=='B'):
        result=result or operand    #or operation
    elif(operator=='C'):
        result=result ^ operator    #xor operation
print(result)