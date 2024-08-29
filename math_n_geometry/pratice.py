class Solution:
    def plusOne(self, digits):
        digits = digits[::-1]
        one , i = 1, 0
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
a = Solution()
digits = [9,9,9]
print(a.plusOne(digits))