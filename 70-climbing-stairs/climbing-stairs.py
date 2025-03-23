"""
4: 

1 step + 1 step + 1 step + 1 step  | 1 step 
2 step + 1 step + 1 step | 1 step 
1 step + 2 step + 1 step | 1 step 
1 step + 1 step + 2 step | 1 step 
2 step + 2 step | 1 step 



"""

class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [0, 1, 2]

        if n <= 2:
            return dp[n]
        
        for i in range(3, n + 1):
            currWays = dp[-1] + dp[-2]
            dp[-2] = dp[-1]
            dp[-1] = currWays
        return dp[-1]
        