class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        res = 0
        start = 0
        while start < len(nums):

            # start of a window
            if nums[start] == 1:

                end = start
                while end < len(nums) and nums[end]:
                    end += 1
                
                res = max(res, end - start)
                start = end
            else:
                start += 1

        return res




