"""
    [] [1,2,3] 
        [1] [2, 3]
            [1, 2] [3]
                [1, 2, 3]
            [1, 3] []

        [2] [3]
            [2, 3] []

        [3]



"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(path, candidates):
        
            res.append(path[:])

            for i in range(len(candidates)):
                path.append(candidates[i])
                dfs(path, candidates[i + 1:])
                path.pop()




        dfs([], nums)
        return res