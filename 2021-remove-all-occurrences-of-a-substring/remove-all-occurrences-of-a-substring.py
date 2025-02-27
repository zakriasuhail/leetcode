class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        stack = []
        for ch in s:

            stack.append(ch)

            # make valid
            while len(stack) >= len(part) and stack[-len(part):] == list(part):

                # pop from stack
                j = len(part)
                while j:
                    stack.pop()
                    j -= 1

        return "".join(stack)
            


        