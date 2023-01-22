class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        mem = []
        for i in range(len(text1)+1):
            mem.append([0 for j in range(len(text2)+1)])

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    mem[i][j] = 1 + mem[i+1][j+1]
                else:
                    mem[i][j] = max(mem[i+1][j], mem[i][j+1])
        return mem[0][0]
