"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
 DO NOT allocate another 2D matrix and do the rotation.

 

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
 
"""

class Solution:
    def rotate(self, matrix) :
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        print(matrix)
        for i in range(len(matrix)):
            print("i is ",i)
            for j in range(i):
                print("j is ",j)
                print(matrix[i][j], matrix[j][i])
                matrix[i][j], matrix[j][i]=matrix[j][i],matrix[i][j]

        return matrix
        
        

a = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(a.rotate(matrix))
        


class Solutions:
    def rotate(self, matrix) :
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        l,r = 0  , len(matrix)-1
        while l<r:
            for i in range(r-l):
                top,bottom = l,r

                # save the left element
                topleft = matrix[top][l+i]

                # save the left bottom elemnet to left top
                matrix[top][l+i]= matrix[bottom-i][l]

                # save bottm right to botton left
                matrix[bottom-i][l]=matrix[bottom][r-i]

                # save top rihit to bottom right
                matrix[bottom][r-i]=matrix[top+i][r] 

                # save topleft to bottom right
                matrix[top+i][r]=topleft
            r-=1
            l+=1

        return matrix

        

a = Solutions()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(a.rotate(matrix))