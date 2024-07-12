"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

from collections import Counter
def topKFrequent(nums,k) :

    hashmap = {}
    res =[]

    freq = [[] for i in range( len(nums)+1)]
       
    for n in nums :
        hashmap[n] = 1+ hashmap.get(n,0)

    for n,c in hashmap.items():
        freq[c].append(n)

    while k:
        pass



    

nums = [1,1,1,2,2,3]
k = 2

print(topKFrequent(nums,k))