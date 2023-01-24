class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #MY SOLUTION, IS MINE!!!!
        # Can be simplified to only use two variables instead 
        # of whole array.

        """
        if len(nums) == 1:
            return nums[0]

        max_money = max(nums[0], nums[1])

        if len(nums) == 2:
            return max_money

        mem = [0 for i in range(len(nums))]
        mem[0] = nums[0]
        mem[1] = nums[1]

        for i in range(2, len(nums)):
            #print(mem)
            mem[i] = max(nums[i]+mem[i-3], nums[i]+mem[i-2])

            max_money = max(mem[i], max_money)
        #print(mem, "EEEND")

        return max_money
        """

        rob1 = 0

        rob2 = 0

        max_money = 0
        
        for i in range(len(nums)):
            max_money = max(rob1+nums[i], rob2)

            rob1 = rob2;

            rob2 = max_money

        return max_money;
