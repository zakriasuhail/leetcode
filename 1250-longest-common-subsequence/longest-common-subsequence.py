"""

  a b c d e
a 1 0 0 0 0
c 0 0 1 0 0
e 0 0 0 0 1 

[0, 0, 0, 0, 0, 0]
[0, 1, 1, 1, 1, 0]
[0, 0, 0, 0, 0, 0] 
[0, 0, 0, 0, 0, 0]

rows = 4
cols = 6

row = 2
col = 4

"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1) + 1
        cols = len(text2) + 1

        # create dp array
        dp = [[0] * cols for _ in range(rows)]

        # iterate
        for row in range(rows - 2, -1, -1):
            for col in range(cols - 2, -1, -1):

                # if have a match
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])
        return dp[0][0]


                




        