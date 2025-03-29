"""The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]"""

class Solution:
    def solveNQueens(self, n: int) :
        column=set()
        posDig= set()#r+c
        nedDiag= set()#r-c
        board = [["."] *n for i  in range(n)] #[['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
        print(board)

        res=[]
        def backtrack(rowIndex):
            if rowIndex==n:
                copy = ["".join(row) for row in board] 
                res.append(copy)
                return
            for colIndex in range(n):
                if colIndex in column or  (rowIndex + colIndex) in posDig or (rowIndex-colIndex) in nedDiag:
                    continue
                column.add(colIndex)
                posDig.add(rowIndex + colIndex)
                nedDiag.add(rowIndex - colIndex)
                board[rowIndex][colIndex]="Q"
                backtrack(rowIndex+1)
                column.remove(colIndex)
                posDig.remove(rowIndex + colIndex)
                nedDiag.remove(rowIndex - colIndex)
                board[rowIndex][colIndex]="."
        backtrack(0)
        return res
a=Solution()
n = 4
print(a.solveNQueens(n))