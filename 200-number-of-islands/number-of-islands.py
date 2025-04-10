class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def getNeighbors(row, col):
            neighbors = []
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dirRow, dirCol in directions:  

                newRow, newCol = dirRow + row, dirCol + col


                if (newRow >= 0 and newRow < rows and
                    newCol >= 0 and newCol < cols and 
                    grid[newRow][newCol] == "1"):
                    neighbors.append((newRow, newCol))
            return neighbors

        def bfs(coord):
            queue = deque([coord])

            while queue:

                row, col = queue.popleft()

                # mark as visited
                grid[row][col] = "0"

                for nr, nc in getNeighbors(row, col):
                    grid[nr][nc] = "0"
                    queue.append((nr, nc))



        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    bfs((row, col))

        return islands

        