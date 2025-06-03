class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        xstring = str(x)

        left, right = 0, len(xstring) - 1
        while left < right:
            if xstring[left] != xstring[right]:
                return False
            left += 1
            right -= 1
        return True

        
        