"""
Problem Statement

A carry is a digit that is transferred to left if sum of digits exceeds 9 while adding two numbers from right-to-left one digit at a time

You are required to implement the following function.

Int NumberOfCarries(int num1 , int num2);

The functions accepts two numbers ‘num1’ and ‘num2’ as its arguments. You are required to calculate and return  the total number of carries generated while adding digits of two numbers ‘num1’ and ‘ num2’.

Assumption: num1, num2>=0"""



def CountOfCarry(num1,num2):
    carry=0
    count=0
    len_a=len(num1)
    len_b=len(num2)
    i=1
    while(len_a!=0 or len_b!=0):
        if(len_a==0):
            sum=int(num2[len(num2)-i])+carry
            len_b-=1
            i+=1
        elif(len_b==0):
            sum=int(num1[len(num1)-i])+carry
            len_a-=1
            i+=1
        else:
            sum=int(num1[len(num1)-i])+int(num2[len(num2)-i])+carry
            i+=1
            len_a-=1
            len_b-=1
        if(sum>=10 and max(len_a,len_b)>0):
            carry=1
            count+=1
        else:
            carry=0
    return count
        
    
    
    
num1=input()
num2=input()
print(CountOfCarry(num1,num2))

