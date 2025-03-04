"""
[2,3,6,7]

    2
        2 2
            2 2 2

            2 2 3
        2 3
            2 3 2


"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        def dfs(path, currSum, currCandidates):
            # base cases
            if currSum == target:
                res.append(path[:])
                return

            # recursive case
            for index, candidate in enumerate(currCandidates):
                if currSum + candidate <= target:
                    path.append(candidate)
                    dfs(path, currSum + candidate, currCandidates[index:])
                    path.pop()

        
        dfs([], 0, candidates)
        return res
        