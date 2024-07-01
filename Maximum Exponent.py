"""You are given a function,

Int MaxExponents (int a , int b);

You have to find and return the number between ‘a’ and ‘b’ ( range inclusive on both ends) which has the maximum exponent of 2.

The algorithm to find the number with maximum exponent of 2 between the given range is

Loop between ‘a’ and ‘b’. Let the looping variable be ‘i’.
Find the exponent (power) of 2 for each ‘i’ and store the number with maximum exponent of 2 so faqrd in a variable , let say ‘max’. Set ‘max’ to ‘i’ only if ‘i’ has more exponent of 2 than ‘max’.
Return ‘max’.
Assumption: a<b"""


def CountExpo(i):
    count=0
    while(i!=0 and i%2==0):
        count+=1
        i=i//2
    return count
    
    
    
def MaximumExpo(a,b):
    max=0
    number=0
    for i in range(a,b+1):
        temp=CountExpo(i)
        if(temp>max):
            max=temp
            number=i
    return number


a,b=map(int,input().split())
print(MaximumExpo(a,b))
