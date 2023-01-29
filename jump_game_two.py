class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        if len(nums) == 1:
            return 0

        mem = [len(nums) for i in range(len(nums))]

        for i in range(len(nums)-2, -1, -1):
            # Try longest jump:
            if nums[i] == 0:
                continue

            longest_jump_pos = i + nums[i]
            if longest_jump_pos >= len(nums) - 1:
                mem[i] = 1
            else:
                mem[i] = 1+mem[longest_jump_pos]
                for j in range(nums[i] - 1, 0, -1):
                    mem[i] = min(1 + mem[i + j], mem[i])
        #print(mem)
        return mem[0]
        """

        furthest = 0
        end = 0
        jumps = 0

        for i in range(len(nums)-1):
            if i + nums[i] > furthest:
                furthest = i + nums[i]

            if end == i:
                jumps += 1
                end = furthest

        return jumps
