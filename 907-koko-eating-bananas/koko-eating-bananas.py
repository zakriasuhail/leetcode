"""

min k: mind
max k: max(piles)



"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def isValid(k):
            hours = 0
            for pile in piles:
                hours += (pile // k)
                if pile % k: hours += 1
            return hours

        
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2

            hours = isValid(mid)
            if hours > h:
                left = mid + 1

            else:
                right = mid

        return right


        