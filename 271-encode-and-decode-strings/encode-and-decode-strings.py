class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        delim = "#"
        encodedString = []
        for string in strs:
            encodedString.append(str(len(string)) + delim)
            encodedString.append(string)
        return "".join(encodedString)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decodedStrings = []
        start = 0
        delim = "#"
        while start < len(s):
            
            # get index
            delimIndex = s.find(delim, start)

            # get number
            stringLength = int(s[start : delimIndex])

            # append string
            decodedStrings.append(s[delimIndex + 1 : delimIndex + 1 + stringLength])

            # update iterator
            start = delimIndex + stringLength + 1

        return decodedStrings

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))