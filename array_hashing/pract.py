
def contain_duplicates(nums):
    hash = set()
    for i in nums:
        if i in hash:
            return True
        hash.add(i)
    return False
from collections import Counter, defaultdict
def valid_anagram(s, t):
    return Counter(s)==Counter(t)

def two_sums(nums,target):
    map={}
    for i in range(len(nums)):
        if target- nums[i] in map:
            return [i, map[target-nums[i]]]
        map[nums[i]] =i
    return map


def group_anagram(strs):
    res= defaultdict(list)
    for char in strs:
        count = [0]*26
        for i in char:
            count[ord(i)- ord("a")]+=1
        res[tuple(count)].append(char)
    return res.values()

def topKFrequent(nums, k):
    freq=[[] for   i in nums]
    map={}
    for  i in nums:
        map[i] =1+ map.get(i,0)
    for key, vak in map.items():
        freq[vak].append(key)
    final=[]

    for i in range(len(freq)-1, -1, -1):
        for c in freq[i]:
            final.append(c)
            if len(final)==k:
                return final


class  Solution:
    def encode(self, list):
        res=""
        for i in list:
            res = res+str(len(i))+"#"+ i
        return res
    
    def decode(self, strs):
        i = 0
        res=[]
        while i < len(strs):
            j=i
            while strs[j]!="#":
                j=j+1
            lenght = int(strs[i:j])
            res.append(strs[j+1: j+1+lenght])
            i = j+1+lenght
        return res
    

def productExceptSelf(nums):
    res=[0]*len(nums)
    prefix =1

    for i in range(len(nums)):
        res[i] = prefix
        prefix = prefix*nums[i]
    postfix =1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= postfix
        postfix = postfix*nums[i]
    return res


def validSudoko(grid):
    rows = defaultdict(set)
    cols = defaultdict(set)
    square = defaultdict(set)
    for r in range(9):
        for c in range(9):
            if grid[r][c]==".":
                continue
            if grid[r][c] in rows[r] and grid[r][c] in cols[c] and grid[r][c] in square[r//3, c//3]:
                return False
            rows[r].add(grid[r][c])
            cols[c].add(grid[r][c])
            square[r//3, c//3].add(grid[r][c])
    return True
def longestConsecutive(nums):
    numset = set(nums)
    longest=0
    for  i in numset:
        if (i-1) not in numset:
            length =0
            while(i+length) in numset:
                length +=1
            longest = max(length, longest)
    return longest


print(longestConsecutive(nums = [2,20,4,10,3,4,5]))
