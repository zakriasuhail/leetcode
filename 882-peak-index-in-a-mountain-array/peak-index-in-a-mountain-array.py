class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        left, right = 0, len(arr) - 1

        while left <= right:

            mid = (left + right) // 2

            leftN = arr[mid - 1] if mid > 0 else -1
            rightN = arr[mid + 1] if mid < len(arr) else -1

            if arr[mid] > leftN and arr[mid] > rightN:
                return mid
            
            elif leftN > arr[mid] > rightN:
                right = mid - 1
            else:
                left = mid + 1
        return -1


        