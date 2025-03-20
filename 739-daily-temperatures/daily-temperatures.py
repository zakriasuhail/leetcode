"""

[73,74,75,71,69,72,76,73]

[(75,2), (72,5), (76,6)]

[1, 1, 4, 2, 1, 1, 0, 0]




"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        minStack = []

        for i, temp in enumerate(temperatures):

            while minStack and minStack[-1][0] < temp:
                prevTemp, prevIndex = minStack.pop()
                output[prevIndex] = i - prevIndex

            minStack.append((temp, i))
        return output

        