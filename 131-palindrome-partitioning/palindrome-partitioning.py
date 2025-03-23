class Solution:
    def isPalindrome(self, string):
        left, right = 0, len(string) - 1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:

        memo = {}
        res = []
        
        def dfs(path, string):
            
            # base cases

            # valid palindromic splits
            if not len(string) and len(path):
                res.append(path[:])
                return

            # recurse
            for i in range(0, len(string)):

                prefix = string[:i + 1]
                suffix = string[i + 1:]

                # prune
                if prefix not in memo:
                    memo[prefix] = self.isPalindrome(prefix)

                if memo[prefix]:
                    path.append(prefix)
                    dfs(path, suffix)
                    path.pop()
                
        dfs([], s)
        return res


        
        