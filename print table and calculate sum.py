"""Problem: Write a program in C to display the table of a number and print the sum of all the multiples in it.
"""

n=int(input())
sum=0
for i in range(1,11):
    print(n*i,end=",")
    sum+=(n*i)
print()
print(sum)