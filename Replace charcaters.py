"""Problem Statement

You are given a function,

Void *ReplaceCharacter(Char str[], int n, char ch1, char ch2);

The function accepts a string  ‘ str’ of length n and two characters ‘ch1’ and ‘ch2’ as its arguments . Implement the function to modify and return the string ‘ str’ in such a way that all occurrences of ‘ch1’ in original string are replaced by ‘ch2’ and all occurrences of ‘ch2’  in original string are replaced by ‘ch1’.

Assumption: String Contains only lower-case alphabetical letters."""


def ReplaceCharacters(s,ch1,ch2):
    new_s=''
    new_s=s.replace(ch1,'*').replace(ch2,ch1).replace('*',ch2)
    return new_s
s=input()
ch1,ch2=map(str,input().split())
print(ReplaceCharacters(s,ch1,ch2))