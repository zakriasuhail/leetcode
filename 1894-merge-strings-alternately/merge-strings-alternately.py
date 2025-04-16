class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        len1, len2 = len(word1), len(word2)
        ptr1 = ptr2 = 0
        output = []

        while ptr1 < len1 or ptr2 < len2:

            if ptr1 < len1 and ptr2 < len2:
                output.append(word1[ptr1])
                output.append(word2[ptr2])
                ptr1 += 1
                ptr2 += 1

            elif ptr1 < len1:
                output.append(word1[ptr1])
                ptr1 += 1
            else:
                output.append(word2[ptr2])
                ptr2 += 1

        return "".join(output)



        