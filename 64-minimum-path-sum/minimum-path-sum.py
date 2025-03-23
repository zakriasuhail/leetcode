"""
[1, 3, 1]
[1, 5, 1]
[4, 2, 1]

[1, 4, 5]
[2, 7, 6]
[6, 6, 7]


[1, 2, 3]
[4, 5, 6]

[1, 0, 0]
[0, 0, 0]

row = 0
col = 1

"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0] * cols for row in range(rows)]

        for row in range(rows):
            for col in range(cols):

                weight = grid[row][col]

                if row - 1 >= 0 and col - 1 >= 0:
                    weightSum = weight + min(dp[row - 1][col], dp[row][col - 1])
                elif row - 1 >= 0:
                    weightSum = weight + dp[row - 1][col]
                elif col - 1 >= 0:
                    weightSum = weight + dp[row][col - 1]
                else:
                    weightSum = weight

                # add to dp matrix
                dp[row][col] = weightSum

        return dp[-1][-1]
        