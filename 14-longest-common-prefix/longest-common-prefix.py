class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        baseWord = strs[0]
        i = 0
        while i < len(baseWord):

            # check all strings
            for string in strs[1:]:
                if i >= len(string) or string[i] != baseWord[i]:
                    return baseWord[:i]
            
            i += 1
        return baseWord

        