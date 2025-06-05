class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        elem = nums[0]
        freq = 0

        for i, num in enumerate(nums):

            if num != elem:

                freq -= 1

                if freq == 0:
                    elem = num
                    freq = 1

            else:

                freq += 1

        return elem


            
