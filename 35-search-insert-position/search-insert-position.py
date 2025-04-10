class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        res = float("inf")
        while left <= right:

            mid = (left + right) // 2

            if nums[mid] >= target:
                res = mid
                right = mid - 1
                
            else:
                left = mid + 1
        return res if res != float("inf") else len(nums)

        