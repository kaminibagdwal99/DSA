"""ou are given a 
m
×
n
m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest than the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Example 1:

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
Example 2:

Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]"""

from collections import deque
class Solution:
    def islandsAndTreasure(self, grid):
        ROW,COL = len(grid), len(grid[0])
        visit = set()
        queue = deque()

        def addRoom(r, c):
            if r<0 or r==ROW or c<0 or c ==COL or grid[r][c]==-1 or (r,c) in visit:
                return
            visit.add((r,c))
            queue.append([r,c])

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==0:
                    queue.append([r,c])
                    visit.add((r,c))
        dist =0
        while queue:
            for i in range(len(queue)) :
                r,c = queue.popleft()
                grid[r][c]=dist

                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r, c-1)
            dist +=1

        return grid

grid = [
  [0,-1],
  [2147483647,2147483647]
]

a = Solution()
print(a.islandsAndTreasure(grid))