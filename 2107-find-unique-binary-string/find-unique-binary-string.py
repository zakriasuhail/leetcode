"""
111
011
001


[x, x, ]



"""
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        numSet = set(nums)
        def dfs(path):
            if len(path) == len(nums[0]):
                if path not in numSet:
                    return path
                else:
                    return None

            return dfs(path + "0") or dfs(path + "1")

        return dfs("")
        




        