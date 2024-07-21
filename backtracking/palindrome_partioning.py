"""
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
"""
class Solution:
    def partition(self, s: str) :
        res = []
        def palindrome(s):
            return s == s[::-1]
        def palindrom_helper(ind, ds):
            if ind == len(s):
                res.append(ds.copy())
                return 
            for i in range( ind, len(s)):
                if palindrome(s[ind:i+1]):
                    palindrom_helper(i +1, ds + [s[ind:i+1]])

        palindrom_helper(0,[])
        return res
a = Solution()

print(a.partition(s = "aab"))