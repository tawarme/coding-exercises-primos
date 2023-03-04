class Solution:
    def letterCombinations1(self, digits: str) -> List[str]:
        if not digits:
            return []

        map = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        res = [digits]
        for i in range(len(digits)):
            d = int(digits[i]) - 2
            childs = []
            for part in res:
                for ch in map[d]:
                    childs.append(part[:i]+ch+part[i+1:])
            res = childs

        return res

    def go(self, s, digits, i, res):
        map = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        if i == len(digits):
            res.append(s)
            return

        for ch in map[int(digits[i]) - 2]:
            self.go(s + ch, digits, i + 1, res)
        

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        self.go("", digits, 0, res)

        return res
