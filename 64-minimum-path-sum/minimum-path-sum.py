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
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if row - 1 >= 0 and col - 1 >= 0:
                    dp[row][col] = grid[row][col] + min(dp[row - 1][col], dp[row][col - 1])
                elif row - 1 >= 0:
                    dp[row][col] = dp[row - 1][col] + grid[row][col]
                elif col - 1 >= 0:
                    dp[row][col] = dp[row][col - 1] + grid[row][col]
                else:
                    dp[row][col] = grid[row][col]
        print(dp)
        return dp[-1][-1]
        