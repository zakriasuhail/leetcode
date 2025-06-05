class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def getNeighbors(r, c):
            dirs = [(1,0), (0,1), (-1, 0), (0, -1)]
            res = []
            for dx, dy in dirs:

                if (
                    0 <= r + dx < len(grid) and
                    0 <= c + dy < len(grid[0]) and
                    grid[r + dx][c + dy] == "1"
                ):
                
                    res.append((r + dx, c + dy))
            return res
                


        def bfs(row, col):

            queue = deque([(row, col)])

            while queue:

                currRow, currCol = queue.popleft()

                # get neighbors
                for nr, nc in getNeighbors(currRow, currCol):
                    queue.append((nr, nc)) 
                    grid[nr][nc] = "0"




        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == "1":
                    # mark visited
                    grid[row][col] = "0"
                    bfs(row, col)
                    islands += 1

        return islands


            
        