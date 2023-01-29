class Solution(object):
    def go(self, n, open, close, current, ans):

        if open < n:
            self.go(n, open+1, close, current + "(", ans)
        
        if close < open:
            self.go(n, open, close+1, current + ")", ans)
        
        if open == close == n:
            ans.append(current)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        open = 0
        close = 0
        current = ""
        ans = []

        self.go(n, open, close, current, ans)

        return ans
