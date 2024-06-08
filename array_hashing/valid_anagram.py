"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""

from collections import Counter

# tc : O(nlogn) sc : o(n)
def valid_anagram(s,t):
    return sorted(s) == sorted(t)

s = "anagram"
t = "nagaram"
print(valid_anagram(s,t))

# tc: o(n) sc: o(1)
def valid_anagram(s,t):
    return Counter(s) == Counter(t)

s = "anagram"
t = "nagaram"
print(valid_anagram(s,t))


# tc: o(n) sc:o(1)
def valid_anagram(s,t):
    if len(s) !=len(t):
        return False
    
    hash_s, hash_t = {}, {}

    for i in range(len(s)):
        hash_s[s[i]] = 1 +hash_s.get(s[i],0)
        hash_t[t[i]] = 1 +hash_t.get(t[i],0)

    for i in hash_s:
        if hash_s[i]==hash_t[i]:return True

    return False


s = "anagram"
t = "nagarame"
print(valid_anagram(s,t))



