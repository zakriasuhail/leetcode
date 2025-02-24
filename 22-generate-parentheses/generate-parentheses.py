"""

    (
((      ()

())


"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []


        def dfs(path, openBracs, closeBracs):
            nonlocal res
            
            # base case
            if openBracs + closeBracs == n * 2:
                res.append(path)
                return

            # recursive
            if openBracs > closeBracs:
                dfs(path + ")", openBracs, closeBracs + 1)
            if openBracs < n:
                dfs(path + "(", openBracs + 1, closeBracs)


        dfs("(", 1, 0)
        return res

        