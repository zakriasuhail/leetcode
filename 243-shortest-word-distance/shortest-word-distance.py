class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        res = float('inf')
        ptr1 = ptr2 = -1

        for i, word in enumerate(wordsDict):

            if word == word1:
                ptr1 = i
            
            elif word == word2:
                ptr2 = i

            if ptr1 != -1 and ptr2 != -1:
                res = min(res, abs(ptr1 - ptr2))
        return res








        






        