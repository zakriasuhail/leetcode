class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        validIndex = 0

        for i, num in enumerate(nums):

            if num != 0:
                nums[validIndex] = num
                validIndex += 1

            
        for i in range(validIndex, len(nums)):
            nums[i] = 0


