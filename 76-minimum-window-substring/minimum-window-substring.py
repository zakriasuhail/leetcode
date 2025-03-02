"""
approach - 1:

- add to window



"""
class Solution:
    def isValid(self, sWindow, tWindow):
        for ch, freq in tWindow.items():
            if sWindow[ch] < freq:
                return False
        return True


    def minWindow(self, s: str, t: str) -> str:

        # init variables
        start = 0
        minWindow = None

        # create window
        window = defaultdict(int)

        # get counter for t
        tWindow = collections.Counter(t)

        # iterate over input string
        for end in range(len(s)):

            ch = s[end]

            # add to window
            window[ch] += 1

            # make window valid
            while self.isValid(window, tWindow):

                # update minimum window found
                if not minWindow:
                    minWindow = s[start:end + 1]

                
                # compare 
                if end - start < len(minWindow):
                    minWindow = s[start : end + 1]

                

                window[s[start]] -= 1
                start += 1
        return minWindow if minWindow else ""
                    






        
        