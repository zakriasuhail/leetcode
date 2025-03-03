"""
nums = 

  [1, 2, 3], k = 3
0 [1, 3, 6]

{
  sum : subarrays
    0 : 1
    




}


"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        psums = {0:1}
        psum = 0
        subarrays = 0
        for num in nums:
            psum += num
            subarrays += psums.get(psum - k, 0)
            psums[psum] = 1 + psums.get(psum, 0)
        return subarrays


        