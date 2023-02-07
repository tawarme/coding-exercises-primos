class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s or not p:
            return False
        
        mem = [[False for col in range(len(p) + 1) ] for row in range(len(s) + 1)]

        mem[0][0] = True

        for i in range(len(p)):
            if p[i] == "*" and mem[0][i - 1]:
                mem[0][i + 1] = True

        for row in range(len(s)):
            for col in range(len(p)):
                if p[col] == ".":
                    mem[row + 1][col + 1] = mem[row][col]

                if p[col] == s[row]:
                    mem[row + 1][col + 1] = mem[row][col]

                if p[col] == "*":
                    # if .*
                    if p[col - 1] != s[row] and p[col - 1] != ".":
                        mem[row + 1][col + 1] = mem[row + 1][col - 1]
                    else:
                        #mem[row][col] = mem[row][col - 1] or mem[row - 1][col] or mem[row][col - 2] # Using mem as reference instead of strings
                        mem[row + 1][col + 1] = mem[row + 1][col] or mem[row][col + 1] or mem[row + 1][col - 1]

        return mem[-1][-1]
