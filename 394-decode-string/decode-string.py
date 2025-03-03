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

            # if we reach a number
            if ch.isdigit():
                
                # get number
                j = i
                while s[j].isdigit():
                    j += 1
                
                num = int(s[i:j])

                stack.append(num)
                i = j - 1

            elif ch == "]":
                string = ""
                while stack[-1] != "[":
                    string = stack.pop() + string
                
                stack.pop()
                num = stack.pop()
                stack.append(string * num)

            else:
                stack.append(ch)

            i += 1
        return "".join(stack)


            





        