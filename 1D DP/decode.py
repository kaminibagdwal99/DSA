"""
A string consisting of uppercase english characters can be encoded to a number using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode a message, digits must be grouped and then mapped back into letters using the reverse of the mapping above. 
There may be multiple ways to decode a message. For example, "1012" can be mapped into:

"JAB" with the grouping (10 1 2)
"JL" with the grouping (10 12)
The grouping (1 01 2) is invalid because 01 cannot be mapped into a letter since it contains a leading zero.

Given a string s containing only digits, return the number of ways to decode it. You can assume that the answer fits in a 32-bit integer.

Example 1:

Input: s = "12"

Output: 2

Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "01"

Output: 0
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i]=="0":
                return 0
            res=dfs(i+1)
            if (i+1<len(s) and (s[i]=="1" or s[i]=="2" and s[i+1] in "0123456")):
                res+=dfs(i+2)
            dp[i]=res
            return res
        return dfs(0)


a ="12"
z = Solution()
print(z.numDecodings(a))