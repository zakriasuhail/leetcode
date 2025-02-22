class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i, num in enumerate(nums):

            # if a valid pair is found
            if target - num in hmap:
                return [i, hmap[target - num]]
            else:
                hmap[num] = i