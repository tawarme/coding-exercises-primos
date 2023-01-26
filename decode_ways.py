class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev = 1
        prevprev = 1

        for i in range(len(s)):
            current = 0
            if s[i-1] == s[i] == "0":
                return 0

            if s[i] != "0":
                current = prev

            if i > 0 and 10 <= int(s[i-1] + s[i]) <= 26:
                current += prevprev

            prevprev = prev
            prev = current


        return prev
