class Solution:
    def getNeighbors(self, row, col, grid):
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        neighbors = []
        for x, y in directions:
            if (row + x >= 0 and row + x < len(grid) and
                col + y >= 0 and col + y < len(grid[0]) and 
                grid[row + x][col + y] == "1"):
                neighbors.append((row + x, col + y))
        return neighbors

    def bfs(self, node, grid):
        queue = deque([node])
        while queue:
            row, col = queue.popleft()
            
            # get neighbors
            for nr, nc in self.getNeighbors(row, col, grid):
                grid[nr][nc] = "0"
                queue.append((nr, nc))


    def numIslands(self, grid: List[List[str]]) -> int:
        



        
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])): 
                if grid[row][col] == "1":
                    islands += 1
                    grid[row][col] = "0"
                    self.bfs((row, col), grid)
        return islands


        