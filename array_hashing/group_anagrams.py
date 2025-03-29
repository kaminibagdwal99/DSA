"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""
from collections import defaultdict
def group_anagram(strs):
    hashmap = defaultdict(list)

    for i in strs:
        count = [0]*26
        for c in i:
            count[ord(c)- ord("a")] +=1

        hashmap[tuple(count)].append(i)
    return hashmap


strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagram(strs))
