class Solution:
    def getNeighbors(self, row, col, grid):
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        neighbors = []
        for x, y in directions:
            if (row + x >= 0 and row + x < len(grid) and
                col + y >= 0 and col + y < len(grid[0]) and 
                grid[row + x][col + y] == "1"):
                grid[row + x][col + y] = "0"
                neighbors.append((row + x, col + y))
        return neighbors


    def numIslands(self, grid: List[List[str]]) -> int:
        
        # run breadth first search
        def bfs(node):
            queue = deque([node])
            while queue:
                row, col = queue.popleft()

                # mark as visited
                grid[row][col] = "0"
                
                # get neighbors
                for neighbor in self.getNeighbors(row, col, grid):
                    queue.append(neighbor)


        
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])): 
                if grid[row][col] == "1":
                    islands += 1
                    bfs((row, col))
        return islands


        