class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            new_a = a ^ b
            b = (a & b) << 1
            a = new_a

        return a