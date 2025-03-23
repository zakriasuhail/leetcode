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
        
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        
        # create dp arrays
        curr = [0] * (len(text1) + 1)
        prev = [0] * (len(text1) + 1)

        # iterate
        for row in range(len(text2) - 1, -1, -1):
            for col in range(len(text1) - 1, -1, -1):

                # if we have a match
                if text1[col] == text2[row]:
                    curr[col] = 1 + prev[col + 1]
                else:
                    curr[col] = max(curr[col + 1], prev[col])
                
            # swap at each row
            curr, prev = prev, curr
        return prev[0]

                




        