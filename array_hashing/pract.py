def contain_duplicates(nums):
    hset=set()
    for i in nums:
        if  i in hset:
            return True
        hset.add(i)
    return False



from collections import Counter, defaultdict
def valid_anagram(s,t):
    return Counter(s)==Counter(t)

def two_sum(nums, target):
    map={}
    for i in range(len(nums)):
        if target-nums[i] in map:
            return [i, map[target-nums[i]]]
        map[nums[i]]=i
    
def group_anagram(strs):
    res=defaultdict(list)
    for char in strs:
        count=[0]*26
        for i in char:
            count[ord(i)-ord("a")]+=1
        res[tuple(count)].append(char)
    return res.values()


def topKFrequent(nums,k):
    count = Counter(nums)
    freq=[[] for i in nums]
    for  key,val in count.items():
        freq[val].append(key)
    res=[]
    for i in range(len(freq)-1, -1, -1):
        for c in freq[i]:
            res.append(c)
            if len(res)==k:
                return res

class Solution:
    def encode(self, list):
        res=""
        for i in list:
            res =res+str(len(i))+"#"+i
        return res
    
    def decode(self,strs):
        res=[]
        i=0
        while i<len(strs):
            j=i
            while strs[j]!="#":
                j=j+1
            length = int(strs[i:j])
            res.append(strs[j+1:j+1+length])
            i=j+1+length
        return res
    
def productExceptSelf(nums):
    prefix=1
    res=[0]* len(nums)
    for i in range(len(nums)):
        res[i]=prefix
        prefix*=nums[i]
    postfix=1
    for i in range(len(nums)-1, -1, -1):
        res[i]*=postfix
        postfix*=nums[i]
    return res



def validSudoko(board):
    row=defaultdict(set) 
    col=defaultdict(set) 
    square=defaultdict(set) 

    for r in range(9):
        for c in range(9):
            if board[r][c] ==".":
                continue
            if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[r//3, c//3]:
                return False
            row[r].add(board[r][c])
            col[c].add(board[r][c])
            square[r//3, c//3].add(board[r][c])
    return True

def longestConsecutive(nums):
    numset = set(nums)
    longest=0
    for i in numset:
        if (i-1) not in numset:
            length=0
            while (i+length) in numset:
                length+=1
            longest=max(longest, length)
    return longest
print(longestConsecutive(nums = [2,20,4,10,3,4,5]))
