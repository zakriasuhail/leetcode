class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        integer = 0
        for index in range(len(s)):
            if index + 1 < len(s) and roman[s[index + 1]] > roman[s[index]]:
                integer -= roman[s[index]]
            else:
                integer += roman[s[index]]
        return integer
