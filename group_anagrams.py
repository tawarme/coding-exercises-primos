class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = {}

        for s in strs:
            memi = {}

            for ch in s:
                memi[ch] = memi.get(ch, 0)
                memi[ch] += 1

            ord = ""
            for let in "abcdefghijklmnopqrstuvwxyz":
                ord += let*memi.get(let,0)

            mem[ord] = mem.get(ord, [])
            mem[ord].append(s)

        return mem.values()
