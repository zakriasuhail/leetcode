class Solution:
    def isValid(self, dict1, dict2):
        for ch, freq in dict1.items():
            if dict2[ch] != freq:
                return False
        return True


    def checkInclusion(self, s1: str, s2: str) -> bool:
        start, end = 0, len(s1)
        dict1 = collections.Counter(s1)
        window = collections.Counter(s2[:end])

        while end < len(s2):

            
            # check window
            if self.isValid(dict1, window):

                return True

            # move
            window[s2[start]] -= 1
            window[s2[end]] += 1
            start += 1
            end += 1
        return self.isValid(dict1, window)





    