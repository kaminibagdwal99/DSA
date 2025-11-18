"""ou are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

"""

class Solution:
    def solve(self, board):
        rows, cols = len(board), len(board[0])
       

        def capture(r,c):
            if r< 0 or c<0 or r ==rows or c==cols or board[r][c]!="O":
                return
            board[r][c]="T"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)

         #capture unsurrounded redion( dfs)(0->T)

        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O" and (r in [0,rows-1] or (c in [0,cols-1])):
                    capture(r,c)

            # capture surrounded region( 0->x)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="T":
                    board[r][c]="O"
        return board



a = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(a.solve(board))
