class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = [-1]

        max_len = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop(-1)

                if len(stack) == 0:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len
