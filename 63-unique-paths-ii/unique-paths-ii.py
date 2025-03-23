"""
[0,0,0]
[0,1,0]
[0,0,0]

[1,1,1]
[1,0,1]
[1,1,2]


[1,0]

"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        # edge case
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0

        for row in range(rows):
            for col in range(cols):
                # if obstacle
                if obstacleGrid[row][col]:
                    obstacleGrid[row][col] = 0
                
                # if space
                else:

                    if row - 1 >= 0 and col - 1 >= 0:
                        obstacleGrid[row][col] = obstacleGrid[row - 1][col] + obstacleGrid[row][col - 1]
                    elif row - 1 >= 0:
                        obstacleGrid[row][col] = obstacleGrid[row - 1][col]
                    elif col - 1 >= 0:
                        obstacleGrid[row][col] = obstacleGrid[row][col - 1]
                    else:
                        obstacleGrid[row][col] = 1
        return obstacleGrid[-1][-1]
                    

