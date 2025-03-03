"""

3[a2[c]]


stack = 3 [ a cc


i = 6
string = "c"
num = 2




"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        i = 0
        while i < len(s):

            ch = s[i]

            if ch == "]":

                # get string
                string = ""
                while stack[-1] != "[":
                    string = stack.pop() + string

                # pop off opening brac
                stack.pop()

                # build number
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                # append string back
                stack.append(int(num) * string)
            
            else:
                stack.append(ch)

            i += 1
        return "".join(stack)






        