"""
obs: 
- need to be lexicographical
- n is length,


params: candidates = "abc", n = 1, k = 3

found = 1
dfs()
    dfs(a) 
        dfs(ab)
            dfs(aba) found: 0 -> 1
            dfs(abc) found: 1 -> 2
        dfs(ac)
            dfs(aca) fond 






"""
class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        found = 0
        result = ""

        def dfs(happyString):
            nonlocal found, result
            if len(happyString) < n:
                for ch in "abc":
                    if happyString and happyString[-1] == ch:
                        continue
                    dfs(happyString + ch)
            
            if len(happyString) > n:
                return

            if len(happyString) == n:
                found += 1
            
                if found == k:
                    result = happyString

              


        dfs("")
        return result
