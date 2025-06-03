"""
sol - 1:
========





abcabcbb


a = 1
b = 1
c = 1
b


abc, cab, 




"""
class Solution:

    def isValid(self, window):
        for ch, freq in window.items():
            if freq > 1:
                return False
        return True



    def lengthOfLongestSubstring(self, s: str) -> int:

        start = end = 0
        res = 0
        window = collections.defaultdict(int)

        while end < len(s):

            # add to window
            window[s[end]] += 1

            # make window valid
            while not self.isValid(window):
                window[s[start]] -= 1
                start += 1

            # update res
            res = max(res, end - start + 1)
            end += 1


        return res





        