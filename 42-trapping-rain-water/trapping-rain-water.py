class Solution:
    def trap(self, height: List[int]) -> int:

        maxes = [] * len(height)

        # get max left
        currMax = 0
        for i in range(len(height)):
            currMax = max(currMax, height[i])
            maxes.append(currMax)

        # get max right
        currMax = 0
        for i in range(len(height) - 1, -1, -1):
            currMax = max(currMax, height[i])
            maxes[i] = min(currMax, maxes[i])
        
        # get total water
        water = 0
        for i, currHeight in enumerate(height):
            water += (maxes[i] - currHeight)
        return water



        
        