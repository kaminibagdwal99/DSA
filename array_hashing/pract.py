from collections import defaultdict
def group_anagram(arr):
    hashmap = defaultdict(list)
    for i in arr:
        count = [0]*26
        for c in i:
            count[ord(c)-ord("a")]+=1
        hashmap[tuple(count)].append(i)
    return hashmap.values()


strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagram(strs))