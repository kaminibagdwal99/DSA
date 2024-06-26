"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        
        for i in s:
            if i.isalnum() :
                res=res+i.lower()
        
        return res ==res[::-1]
            


s = "A man, a plan, a canal: Panama"
a = Solution()
# print(a.isPalindrome(s))



class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l<r:
            while l<r and not self.isalnum(s[l]):
                l+=1
            while r>l and not self.isalnum(s[r]):
                r-=1
           
            if s[l].lower()!=s[r].lower():
                return False
            l = l+1
            r = r-1
        return True
        
        
        
    def isalnum(self,c):
        return (
            ord("A")<=ord(c)<=ord("Z") or 
            ord("a")<=ord(c)<=ord("z") or
            ord("0")<=ord(c)<=ord("9")


        )
            


s = "A man, a plan, a canal: Panama"
a = Solution()
print(a.isPalindrome(s))