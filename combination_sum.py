# This excercise is different to the one the refers to
# TODO: Review video excercise in the future

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        mem = [0 for mem in range(target + 1)]
        mem[0] = 1


        """
        0 1 2 3 4 5  6
        1 1 2 4 7 20
            3

        0+3 1
        1+2 2
        2+1 1"""

        for i in range(1, target + 1):
            #print(mem)
            for j in range(len(nums)):
                if nums[j] <= i:
                    mem[i] += mem[i - nums[j]]

        return mem[-1]
