from collections import deque
def numIslands(grid):
    rows, cols  = len(grid), len(grid[0])
    visit = set()
    res=0
    def dfs(r,c):
        q  = deque()
        q.append([r,c])
        visit.add((r,c))

        while q:
            dr, dc = q.popleft()
            directions = [[1,0], [0,1], [0,-1] , [-1,0]]
            for row, col in directions:
                sr, sc = dr+row, dc+col
                if sr in range(rows) and sc in range(cols) and grid[sr][sc]=="1" and ((sr,sc)) not in visit:
                    q.append([sr,sc])
                    visit.add((sr,sc))
    

    for r in range(rows):
        for c in range(cols):
            if grid[r][c]=="1" and (r,c) not in visit:
                dfs(r,c)
                res +=1
    return res
def maxAreaOfIsland(grid):
    rows, cols = len(grid), len(grid[0])
    area=0

    def dfs(r,c):
        q = deque()
        q.append([r,c])
        grid[r][c]=0
        res=1
        while q:
            dr, dc = q.popleft()
            directions = [[1,0], [0,1], [0,-1], [-1,0]]
            for row, col in directions:
                sr, sc = dr+row, dc+col
                if sr in range(rows) and sc in range(cols) and grid[sr][sc]==1:
                    grid[sr][sc]=0
                    q.append([sr, sc])
                    res+=1
        return res
    


    for r in range(rows):
        for c in range(cols):
            if grid[r][c]==1:
                area = max(area, dfs(r,c))
    return area

def islandsAndTreasure(grid):
    visit =set()
    rows, cols = len(grid), len(grid[0])
    q = deque()

    def addRoom(r,c):
        if r not in range(rows) or c not in range(cols) or grid[r][c]==-1 or (r,c) in visit:
            return
        visit.add((r,c))
        q.append([r,c])
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] ==0:
                q.append([row,col])
                visit.add((row,col))
    dist=0
    while q:
        for i in range(len(q)):
            r,c = q.popleft()
            grid[r][c]=dist
            addRoom(r+1, c)
            addRoom(r-1, c)
            addRoom(r, c+1)
            addRoom(r, c-1)
        dist+=1
    return grid



grid = [
  [0,-1],
  [2147483647,2147483647]
]
def orangesRotting(grid):
    rows , cols = len(grid), len(grid[0])
    q = deque()
    time =fresh =0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c]==1:
                fresh+=1
            if grid[r][c]==2:
                q.append([r,c])
    directions = [[1,0], [0,1], [0,-1], [-1,0]]
    while q and fresh>0:
        for i in range(len(q)):
            r,c = q.popleft()
            for dr, dc in directions:
                row , col = dr+r, dc+c
                if row not in range(rows) or col not in range(cols) or grid[row][col]!=1:
                    continue
                grid[row][col]=2
                q.append([row,col])
                fresh=fresh-1
        time+=1
    return time if fresh==0 else -1

print(orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]))

