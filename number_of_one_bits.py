class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        one_counter = 0
        for i in range(32):
            if n & 1 << i:
                one_counter += 1
        
        return one_counter
