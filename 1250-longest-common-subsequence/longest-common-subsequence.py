"""

  a c e 0
a 3     0
b   2 . 0
c   2 1 0
d   . 1 0
e   . 1 0
  0 0 0 0


"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if len(text2) < len(text1):
            text1, text2 = text2, text1

        
        curr = [0] * (len(text1) + 1)
        prev = [0] * (len(text1) + 1)

        for i in range(len(text2) - 1, -1, -1):
            for j in range(len(text1) -1, -1, -1):
                
                if text1[j] == text2[i]:
                    curr[j] = 1 + prev[j + 1]
                else:
                    curr[j] = max(curr[j + 1], prev[j])

            curr, prev = prev, curr
        return prev[0]



        