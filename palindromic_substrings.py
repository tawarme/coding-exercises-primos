class Solution:
    def check(self, left, right, s):
        c = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -=1
            right += 1
            c += 1

        return c

    def countSubstrings(self, s: str) -> int:
        c=0
        for i in range(len(s)):
            #pair
            c += self.check(i, i+1, s)
            #odd
            c += self.check(i, i, s)

        return c
