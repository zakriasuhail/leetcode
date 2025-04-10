class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        elem = nums[0]
        count = 1

        for num in nums[1:]:

            if num == elem:
                count += 1
            
            else:
                count -= 1

                if count < 0:
                    elem = num
                    count = 0
        return elem
        