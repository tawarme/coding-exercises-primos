class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        elif len(s) == 0:
            return 0

        mem = {}

        max_len = 0
        start_i = 0
        for i in range(len(s)):
            if mem.get(s[i]):
                cur_len = i - start_i
                max_len = max(max_len, cur_len)

                while mem.get(s[i]):
                    del mem[s[start_i]]
                    start_i += 1

            mem[s[i]] = True


        max_len = max(max_len, len(s) - start_i)

        return max_len
