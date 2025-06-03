"""
-1, 0, 1, 2, -1, -4

-4, -1, -1, 0, 1, 2


"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.add(tuple([nums[i], nums[left], nums[right]]))
                    left += 1
                    right -= 1

                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1

        return list(res)