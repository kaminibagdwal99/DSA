"""
You are given a string s consisting of lowercase english letters.

We want to split the string into as many substrings as possible, while ensuring that each letter appears in at most one substring.

Return a list of integers representing the size of these substrings in the order they appear in the string.

Example 1:

Input: s = "xyxxyzbzbbisl"

Output: [5, 5, 1, 1, 1]
Explanation: The string can be split into ["xyxxy", "zbzbb", "i", "s", "l"].

Example 2:

Input: s = "abcabc"

Output: [6]"""

class Solution:
    def partitionLabels(self, s: str) :
        lastIndex ={}

        for i,c in enumerate(s):
            lastIndex[c]=i
        print(lastIndex)
        res =[]
        size = 0
        end=0
        for i,c in enumerate(s):
            size+=1
            end=max(end, lastIndex[c])

            if i ==end:
                res.append(size)
                size=0
        return res



a = Solution()
print(a.partitionLabels(s = "xyxxyzbzbbisl"))
