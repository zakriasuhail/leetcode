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
                res.append("".join(path))
                return

            # recursive
            if openBracs > closeBracs:
                path.append(")")
                dfs(path, openBracs, closeBracs + 1)
                path.pop()
            if openBracs < n:
                path.append("(")
                dfs(path, openBracs + 1, closeBracs)
                path.pop()


        dfs(["("], 1, 0)
        return res

        