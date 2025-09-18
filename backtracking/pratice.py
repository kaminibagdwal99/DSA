


def subsets(nums):
    res=[]
    def dfs(i,ds):
        if i >= len(nums):
            res.append(ds.copy())
            return 
        dfs(i+1, ds+ [nums[i]])
        dfs(i+1, ds)
    dfs(0, [])
    return res

def combinationSum(candidates, target):
    res=[]
    def dfs(i, ds, target):
        if target==0:
            res.append(ds.copy())
            return 
        if i==len(candidates):
            return
        if candidates[i]<=target:
            dfs(i, ds+[candidates[i]], target-candidates[i])
        dfs(i+1, ds, target)
    dfs(0,[],target)
    return res


def combinationSum2(candidates, target):
    candidates.sort()
    res=[]
    def dfs(index, ds, target):
        if target==0:
            res.append(ds.copy())
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i]==candidates[i-1]:
                continue
            if candidates[i]>target:
                break
            dfs(i+1, ds+[candidates[i]], target-candidates[i])
    dfs(0, [],target)
    return res
def permute(nums):
    res=[]
    def dfs(ind, ds):
        if ind >= len(nums):
            res.append(ds.copy())
            return
        for i in range(ind, len(nums)):
            nums[ind], nums[i]=nums[i], nums[ind]
            dfs(ind+1, ds+[nums[ind]])
            nums[ind], nums[i]=nums[i], nums[ind]
    dfs(0,[])
    return res


def subsetsWithDup(nums):
    res=[]
    nums.sort()
    def dfs(ind,ds):
        res.append(ds)
        for i in range(ind, len(nums)):
            if i>ind and nums[i]==nums[i-1]:
                continue
            dfs(i+1, ds+ [nums[i]])
    dfs(0, [])
    return res


def partition(s):
    res=[]
    def panlindrome(s):
        return s==s[::-1]
    def dfs(ind, ds):
        if ind>= len(s):
            res.append(ds.copy())
            return
        for i in range(ind, len(s)):
            if panlindrome(s[ind:i+1]):
                dfs(i+1, ds+[s[ind:i+1]])
    dfs(0, [])
    return res

def letterCombinations(digits):
    res=[]
    digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
    def dfs(ins, ds):
        if len(ds)==len(digits):
            res.append(ds)
            return
        
        for c in digitToChar[digits[ins]]:
            dfs(ins+1, ds+c)
    dfs(0,"")
    return res
print(letterCombinations(digits = "34"))