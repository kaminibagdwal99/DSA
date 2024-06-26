"""
You are given a large integer represented as an integer array digits, where each digits[i] is the
ith digit of the integer. The digits are ordered from most significant to least significant in
left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""
# tc : o(n) sc: o(n)
class Solution:
    def plusOne(self, digits) :
        
        number = int("".join(str(x) for x in digits))
        number +=1
        return  [int(x) for x in str(number)]
       


a = Solution()
digits = [1,2,3]
print(a.plusOne(digits))


# optimal solution  tc: o(n) sc :o(1)
class Solutions:
    def plusOne(self, digits) :
        digits = digits[::-1]
        one,i = 1,0
        while one:
            if i < len(digits):
                if digits[i]==9:
                    digits[i]=0
                else:
                    digits[i]+=1
                    one = 0
            else:
                digits.append(1)
                one = 0
            i+=1
        return digits[::-1]


       


a = Solutions()
digits = [9,9,9]
print(a.plusOne(digits))


