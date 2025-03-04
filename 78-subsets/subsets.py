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
        
        def dfs(path, index):
        
            res.append(path[:])

            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(path, i + 1)
                path.pop()




        dfs([], 0)
        return res