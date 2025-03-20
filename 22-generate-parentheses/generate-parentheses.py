"""
n = 3

""



"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def gen(path, openBracs, closeBracs):

            # base cases
            if openBracs == n and closeBracs == n:
                res.append("".join(path))
                return

            # recursive cases
            if closeBracs < openBracs:
                path.append(")")
                gen(path, openBracs, closeBracs + 1)
                path.pop()

            if openBracs <= n:
                path.append("(")
                gen(path, openBracs + 1, closeBracs)
                path.pop()


        
        gen(["("], 1, 0)
        return res



            
        