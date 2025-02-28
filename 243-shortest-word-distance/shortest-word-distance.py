class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1Indices = []
        word2Indices = []
        for i, word in enumerate(wordsDict):
            if word == word1:
                word1Indices.append(i)
            elif word == word2:
                word2Indices.append(i)
        
        res = float("inf")
        for word1Indice in word1Indices:
            for word2Indice in word2Indices:
                res = min(res, abs(word2Indice - word1Indice))
        return res


        