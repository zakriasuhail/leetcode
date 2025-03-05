class Solution:
    def search(self, nums, target, first):
        res = -1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                res = mid
                if first:
                    right = mid - 1
                else:
                    left = mid + 1

            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return res




    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.search(nums, target, 1), self.search(nums, target, 0)]



        