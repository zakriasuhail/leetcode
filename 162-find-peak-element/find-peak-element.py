class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            leftN = float("-inf") if mid == 0 else nums[mid - 1]
            rightN = float("-inf") if mid == len(nums) - 1 else nums[mid + 1]

            print(leftN, nums[mid], rightN)
            if nums[mid] > leftN and nums[mid] > rightN:
                return mid
            
            elif leftN >= nums[mid] >= rightN:
                right = mid - 1
            else:
                left = mid + 1
        return 

        

        