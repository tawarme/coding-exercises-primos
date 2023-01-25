class Solution(object):
    def max_rob(self, start, end, max_money, nums):
        rob1 = 0
        rob2 = 0
        #max_money = 0

        for i in range(start, end):
            max_money = max(rob2, nums[i]+rob1)
            rob1 = rob2
            rob2 = max_money

        return max_money

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(self.max_rob(0, len(nums)-1, 0, nums), 
                   self.max_rob(1, len(nums), nums[0], nums))
