"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'."""
from collections import deque
class Solution:
    def numIslands(self, grid) :
        if not grid :
            return 0
        rows,cols=len(grid),len(grid[0])
        visit = set()
        island =0

        def bfs(r,c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))
            print(f"visit is {visit}")

            while q:
                row,col = q.popleft()
                directions = [[1,0], [-1,0],[0,1], [0,-1]]
                for dr,dc in directions:
                    r = row+ dr
                    c = col+ dc
                    if r in range(rows) and c in range(cols) and grid[r][c]=="1" and (r,c) not in visit:
                        q.append((r,c))
                        visit.add((r,c))                      

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]== "1" and (row,col) not in visit:
                    print(f"row is{row},col is {col}")
                    bfs(row,col)
                    island +=1
        return island
                    
            


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
a = Solution()
print(a.numIslands(grid))