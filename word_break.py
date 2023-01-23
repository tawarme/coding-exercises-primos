class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hash_wordDict = {}

        for word in wordDict:
            hash_wordDict[word] = True

        mem = [True]

        for i in range(1, len(s) + 1):
            word_breakable = False

            for j in range(i-1, -1, -1):
                if mem[j] and hash_wordDict.get(s[j:i], False):
                    word_breakable = True
                    break

            mem.append(word_breakable)
            

        return mem[-1]
