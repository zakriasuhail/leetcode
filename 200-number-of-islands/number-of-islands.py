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

        
    def dfs(self, row, col, grid):
        if (row < 0 or row >= len(grid) or
            col < 0 or col >= len(grid[0]) or 
            grid[row][col] == "0"):
            return
        
        # mark as visited
        grid[row][col] = "0"

        # traverse
        self.dfs(row + 1, col, grid)
        self.dfs(row - 1, col, grid)
        self.dfs(row, col + 1, grid)
        self.dfs(row, col - 1, grid)
        


    def numIslands(self, grid: List[List[str]]) -> int:  
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])): 
                if grid[row][col] == "1":
                    islands += 1
                    self.dfs(row, col, grid)
        return islands


        