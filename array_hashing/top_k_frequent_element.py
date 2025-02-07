"""
Given an integer array nums and an integer k, return the k most frequent elements.
 You may return the answer in any order.

 

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
    freq = [[] for i in range( len(nums)+1)] #[[] ,[], [], [], [], [], []]
    
    for n in nums :
        hashmap[n] = 1+ hashmap.get(n,0) #{1: 3, 2: 2, 3: 1}

    for n,c in hashmap.items():
        freq[c].append(n) #[[], [3], [2], [1], [], [], []]
    
    res = []

    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res)==k:
                return res    

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums,k))

# this is done using Counter


# from collections import Counter
# def topKFrequent(nums, k):
#     freq = [[] for _ in range(len(nums)+1)]
#     a = Counter(nums)
#     for key, v in a.items():
#         freq[v].append(key)

    
#     res = []
#     for i in range(len(freq)-1, 0, -1):
#         for n in freq[i]:
#             res.append(n)
#             if len(res)==k:
#                 return res    


    
# nums = [1,1,1,2,2,3]
# k = 2

# print(topKFrequent(nums,k))