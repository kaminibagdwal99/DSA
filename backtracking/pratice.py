class Solution:
    def subsets(self, nums):
        res=[]
        subset =[]
        def subset_helper(i):
            if i>= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            subset_helper(i+1)
            subset.pop()
            subset_helper(i+1)
        subset_helper(0)
        return res
    
    def combinationSum(self, candidates, target):
        res = []
        def helper(i,sum,target):
            if target==0:
                res.append(sum)
                return
            if i==len(candidates):
                return
            if candidates[i]<=target:
                helper(i, sum+[candidates[i]], target-candidates[i])
            helper(i+1,sum,target)
        helper(0,[],target)
        return res
    
    def combinationSum2(self, candidates, target):
        res =[]
        candidates.sort()
        def helper(ind, ds, target):
            if target==0:
                res.append(ds)
                return
            for i in range(ind,len(candidates)):
                if candidates[i]==candidates[i-1] and i > ind:
                    continue
                if candidates[i]>target:
                    break
                helper(i+1, ds +[candidates[i]], target-candidates[i])
        helper(0,[],target)
        return res
    
    def permute(self,nums):
        res=[]
        def helper(index):
            if index==len(nums):
                res.append(nums[:])
                return 
            for i in range(index, len(nums)):
                nums[index], nums[i]=nums[i], nums[index]
                helper(index+1)
                nums[index], nums[i]=nums[i], nums[index]
        helper(0)
        return res
    
    def subsetsWithDup(self, nums):
        nums.sort()
        res=[]
        def helper(ind, ds):
            
            res.append(ds)
            
            for i in range(ind,len(nums)):
                if i>ind and nums[i]==nums[i-1]:continue
                helper(i+1,ds+[nums[i]])
        helper(0,[])
        return res
    
    def partition(self, s):
        res=[]
        def ispalindrome(s):
            return s==s[::-1]

        def helper(ind, ds):
            if ind==len(s):
                res.append(ds.copy())
                return
            
            for i in range(ind, len(s)):
                if ispalindrome(s[ind:i+1]):
                    helper(i+1 ,ds + [s[ind:i+1]])
        helper(0,[])
        return res
    
    def letterCombinations(self, digits):
        res=[]
        digit_char={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqr",
            "8":"stv",
            "9":"wxyz"
        }
        def helper(ind,ds):
            if len(ds)==len(digits):
                res.append(ds)
                return
            for i in digit_char[digits[ind]]:
                helper(ind+1, ds+i)
        if digits:
            helper(0,"")
        return res



a = Solution()
print(a.letterCombinations(digits = "34"))