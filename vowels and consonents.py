# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 19:00:53 2024

@author: sushm
"""

#finding no of vowels and consonents in a paragraph

s=input()
vowel,consonent=0,0
for i in range(len(s)):
    if(s[i] in "aeiou"):
       vowel+=1
    else:
        consonent+=1
print(f"Number of vowels: {vowel}")
print(f"Number of consonents: {consonent}")
       