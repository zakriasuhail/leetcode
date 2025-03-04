class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        combs = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            '8' : "tuv",
            "9" : "wxyz",
        }


        res = []
        def dfs(path, digits):
            if not len(digits):
                res.append("".join(path))
                return

            for character in combs[digits[0]]:
                path.append(character)
                dfs(path, digits[1:])
                path.pop()

        if not digits:
            return []
        dfs([], digits)
        return res