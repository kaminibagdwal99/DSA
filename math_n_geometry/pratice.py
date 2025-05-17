class Solution:
    def rotate(Self, matrix):
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]
        return matrix
    
    def setZeroes(self, matrix):
        pair = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    pair.append([i,j])
        for p in pair:
            r,c= p
            for i in range(len(matrix)):
                matrix[i][c]=0
            for i in range(len(matrix[0])):
                matrix[r][i]=0
        return matrix
    
    def isHappy(self, n):
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sum_square(n)
            if n ==1:
                return True
        return False
    def sum_square(self, n):
        o = 0
        while n :
            o = o+ (n%10)**2
            n = n//10
        return o
    
    def plusOne(self, digits):
        digits = digits[::-1]
        one =1
        i = 0
        while one:
            if i < len(digits):
                if digits[i]==9:
                    digits[i]=0
                else:
                    digits[i]+=1
                    one =0
            else:
                digits.append(1)
                one=0
            i =i+1
        return digits[::-1]
    
    def myPow(self, x, n):
        number = abs(n)
        total=1
        while number>1:
            if number%2==0:
                x= x*x
                number= number//2
            else:
                total = total*x
                number= number-1
        return x*total if n>0 else 1/(x*total)


a = Solution()
x = 2.00000; n = 10
print(a.myPow(x,n))