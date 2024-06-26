"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""



class Solution:
    def setZeroes(self, matrix) :
        """
        Do not return anything, modify matrix in-place instead.
        """
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




a = Solution()

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(a.setZeroes(matrix))

class Solutions:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        first_row_zero = first_col_zero = False
        
        # Determine if the first row or first column should be zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        
        # Use the first row and column to mark zeros
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Zero out cells based on markers in the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Zero out the first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Zero out the first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
        
        return matrix

# Example usage
a = Solutions()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(a.setZeroes(matrix))
