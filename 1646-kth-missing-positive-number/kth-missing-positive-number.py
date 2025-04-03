"""
brute:
- convert into a set
- iterate from 1 to len(arr)

opt:
- count skipped numbers
- iterate and compare index + 1 to arr[index] to get current skipped

arr = 
[2,3,4,7,11]
 1 1 1 3 6

TC: O(n)
SC: O(1)

"""
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        for i, num in enumerate(arr):

            if (num - (i + 1)) >= k:
                lastNum = arr[i-1]
                lastSkipped = lastNum - i
                return lastNum + (k - lastSkipped)
        return len(arr) + k

        