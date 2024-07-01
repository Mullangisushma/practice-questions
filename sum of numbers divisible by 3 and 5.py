"""You are required to implement the following function:

Int Calculate(int m, int n);

The function accepts 2 positive integer ‘m’ and ‘n’ as its arguments.You are required to calculate the sum of numbers divisible both by 3 and 5, between ‘m’ and ‘n’ both inclusive and return the same.
Note
0 < m <= n"""

m=int(input())
n=int(input())
lst=[]
for i in range(m,n+1):
    if(i%3==0 and i%5==0):
        lst.append(i)
print(sum(lst))
