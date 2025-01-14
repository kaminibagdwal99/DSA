"""You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
If this is impossible, return -1.

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 """
from collections import deque
class Solution:
    def orangesRotting(self, grid):
        q = deque()
        ROWS,COLS = len(grid), len(grid[0])
        time, fresh = 0,0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] ==1:
                    fresh +=1
                if grid[i][j] ==2:
                    q.append([i,j])
        directions =[[0,1], [0,-1], [1,0], [-1,0]]

        while q and fresh>0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row,col = r+dr, c+dc

                    if (row<0 or row==ROWS or col <0 or col == COLS or grid[row][col] != 1):
                        continue
                    grid[row][col]=2
                    q.append([row,col])
                    fresh -=1
            time +=1
        return time if fresh ==0 else -1

a = Solution()
print(a.orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]))