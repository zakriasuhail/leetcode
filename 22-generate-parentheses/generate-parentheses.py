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
                res.append(path)
                return

            # recursive cases
            if closeBracs < openBracs:
                gen(path + ")", openBracs, closeBracs + 1)

            if openBracs <= n:
                gen(path + "(", openBracs + 1, closeBracs)
        
        gen("(", 1, 0)
        return res



            
        