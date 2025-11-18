from collections import deque


def numIslands(grid):
    rows , cols = len(grid), len(grid[0])
    visit=set()
    island =0
    def dfs(r,c):
        q = deque()
        q.append([r,c])
        visit.add((r,c))
        while q:
            row, col = q.popleft()
            directions = [[1,0], [0,1], [0,-1], [-1,0]]
            for dr, dc in directions:
                sr, sc = row+dr, dc+col
                if sr in range(rows) and sc in range(cols) and grid[sr][sc]=="1" and (sr,sc) not in visit:
                    q.append([sr,sc])
                    visit.add((sr,sc))
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]=="1" and (r,c) not in visit:
                dfs(r,c)
                island =island+1
    return island

def maxAreaOfIsland(grid):
    rows, cols = len(grid), len(grid[0])
    area=0
    def bfs(r,c):
        grid[r][c]=0
        q=deque()
        q.append([r,c])
        res=1
        while q:
            row,col = q.popleft()
            direction=[[1,0], [0,1], [0,-1], [-1,0]]
            for dr, dc in direction:
                sr,sc = row+dr, col+dc
                if sr in range(rows) and sc in range(cols) and grid[sr][sc]==1:
                    grid[sr][sc]=0
                    q.append([sr,sc])
                    res=res+1
        return res

    for r in range(rows):
        for c in range(cols):
            if grid[r][c]==1:
                area = max(area,bfs(r,c))
    return area

def islandsAndTreasure(grid):
    rows , cols = len(grid), len(grid[0])
    visit = set()
    q = deque()

    def addroom(r,c):
        if r in range(rows) and c in range(cols) and grid[r][c]==2147483647 and (r,c) not in visit:
                    
                    q.append([r,c])
                    visit.add((r,c))
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]==0:
                q.append([r,c])
                visit.add((r,c))

    dist=0
    while q:
        for i in range(len(q)):
            r,c = q.popleft()
            grid[r][c]=dist
            addroom(r+1, c)
            addroom(r-1,c)
            addroom(r,c+1)
            addroom(r,c-1)
        dist+=1
    return grid

grid = [
  [0,-1],
  [2147483647,2147483647]
]

print(islandsAndTreasure(grid))