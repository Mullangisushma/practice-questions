"""Write a program in C such that it takes a lower limit and upper limit as inputs and print all the intermediate palindrome numbers."""

num1=int(input())
num2=int(input())

for i in range(num1+1,num2):
    reverse=0
    temp=i
    while(temp!=0):
        remainder=temp%10
        reverse=reverse*10+remainder
        temp=temp//10
    if(i==reverse):
        print(i,end=" ")