import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.sub(r"[^a-z0-9]", "", s)

        for i in range(len(s)):
            if s[i] != s[len(s)-i - 1]:
                return False
        
        return True
