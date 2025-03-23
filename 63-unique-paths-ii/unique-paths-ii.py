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

        dp = [[0] * cols for row in range(rows)] 

        # edge case
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0

        for row in range(rows):
            for col in range(cols):
                # if obstacle
                if obstacleGrid[row][col]:
                    dp[row][col] = 0
                
                # if space
                else:

                    if row - 1 >= 0 and col - 1 >= 0:
                        dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
                    elif row - 1 >= 0:
                        dp[row][col] = dp[row - 1][col]
                    elif col - 1 >= 0:
                        dp[row][col] = dp[row][col - 1]
                    else:
                        dp[row][col] = 1
        return dp[-1][-1]
                    

