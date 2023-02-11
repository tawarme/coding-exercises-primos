class Solution:
    def checkPalindrome(self, string, left, right):
        # 0123
        # abcd
        #-----
        lenght = 0
        while True:
            if not (left >= 0 and right <= len(string) - 1) or string[left] != string[right]:
                break
            
            lenght = right - left + 1

            left -= 1
            right += 1

        return lenght

    def longestPalindrome(self, s: str) -> str:

        if not s:
            return ""

        palin_i = 0
        palin_len = 1

        for i in range(len(s)):
            odd_len = self.checkPalindrome(s, i, i)
            even_len = self.checkPalindrome(s, i, i+1)

            max_len = max(odd_len, even_len)

            if palin_len < max_len:
                palin_len = max_len
                palin_i = i

        left = palin_i - (palin_len-1)//2
        right = palin_i + palin_len//2
        
        return s[left: right + 1]

