class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0
        max = nums[0]
        for num in nums:
            if cur < 0:
                cur = 0
            
            cur += num

            if cur > max:
                max = cur

        return max
