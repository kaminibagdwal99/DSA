"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]"""

class Solution:
    def combinationSum2(self, candidates, target: int) :
        res = []
        candidates.sort()
         
        def conbination_helper(ind, ds, target):
            if target == 0:
                res.append(ds)
                return 
            for i in range(ind, len(candidates)):
                if i > ind and candidates[i-1]==candidates[i]:
                    continue
                if candidates[i]>target:
                    break
                
                conbination_helper(i+1, ds + (([candidates[i]])) , target-candidates[i],)
        conbination_helper(0, [], target)
        return  res


a = Solution()
print(a.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))