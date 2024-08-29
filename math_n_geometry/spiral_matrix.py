"""
Given an m x n matrix, return all elements of the matrix in spiral order.
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
"""
# tc : o(n*m) sc: o(1)
class Solution:
    def spiralOrder(self, matrix) :
        l,r = 0, len(matrix[0])
        t,b = l,len(matrix)
        res =[]
        while l<r and t<b: 
            # get every ith element in  top row
            for i in range(l,r):
                res.append(matrix[t][i])
            t +=1
            # get every elemnt from right from top to bottom
            for i in range(t,b):
                res.append(matrix[i][r-1])
            r-=1
            # get every elemnt in bottom row
            if not l<r and t<b:
                break
            for i in range(r-1,l-1,-1):
                res.append(matrix[b-1][i])
            b -=1

            for i in range(b-1,t-1,-1):
                res.append(matrix[i][l])
            l+=1
        return res

a = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(a.spiralOrder(matrix))