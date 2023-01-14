class Solution:
    def reverseBits(self, n: int) -> int:
        rev_num = 0
        # My solution
        # is mine!

        # for i in range(16):
        #     rev_num |= (n & 1<<i) << (32 - 2*i - 1)

        # for i in range(16, 32):
        #     rev_num |= (n & 1<<i) >> (2*i - 32 + 1) 
        # return rev_num

        for i in range(32):
            rev_num <<= 1
            rev_num |= (n & 1)
            n >>= 1

        return rev_num
