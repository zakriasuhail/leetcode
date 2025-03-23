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
        # create dp array
        rows = len(text2) + 1
        cols = len(text1) + 1
        dp = [[0] * cols for _ in range(rows)]

        # iterate with bottomup approach
        for row in range(len(text2) - 1, -1, -1):
            for col in range(len(text1) - 1, -1, -1):

                # if current characters match
                if text1[col] == text2[row]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                
                # if we either went down or right
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])
        print(dp)
        return dp[0][0]


                




        