class Solution:
    def romanToInt(self, s: str) -> int:
        conversions = {"I": 1,
                      "V": 5,
                      "X": 10,
                      "L": 50,
                      "C": 100,
                      "D": 500,
                      "M": 1000}
        special_conversion = ["IV", "IX", "XL", "XC", "CD", "CM"]
        
        num = 0
        skip = False
        for i in range(len(s)):
            if skip:
                skip = False
                continue
            if i+1 < len(s) and s[i:i+1+1] in special_conversion:
                num += (conversions[s[i+1]] - conversions[s[i]])
                skip = True
            else:
                num += conversions[s[i]]

        return num
