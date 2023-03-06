class Solution:
    def characterReplacement(self, s: str, k: int) -> int:  
        mem = {}

        max_len = 0
        start = 0
        top_char = ""
        for i in range(len(s)):
            ch = s[i]
            lenght = i - start + 1
            
            mem[ch] = mem.get(ch, 0)
            mem[ch] += 1
            #print(mem, s[start:i+1])

            if ch == top_char:
                max_len = max(max_len, lenght)
                continue

            if mem[ch] > mem.get(top_char, 0):
                top_char = ch

            while i - start + 1 > mem[top_char] + k:
                ex_ch = s[start]
                mem[ex_ch] -= 1

                if ex_ch == top_char:
                    for ch, count in mem.items():
                        if count > mem[ex_ch]:
                            top_char = ch

                start += 1

            max_len = max(max_len, i - start + 1)

            #if length > mem[top_char] + k:

        return max_len