class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # save space
        if len(word2) < len(word1):
            word1, word2 = word2, word1

        # declare dp arrays
        curr = [1] * (len(word1) + 1)
        prev = [i for i in range(len(word1), -1, -1)]

        # solve subproblems
        for row in range(len(word2) - 1, -1, -1):
            for col in range(len(word1) - 1, -1, -1):

                # if char are the same
                if word1[col] == word2[row]:
                    curr[col] = prev[col + 1]
                else:
                    curr[col] = 1 + min(curr[col + 1], prev[col], prev[col + 1])

            curr, prev = prev, curr
            curr[-1] = len(word2) - row + 1

        return prev[0]

         