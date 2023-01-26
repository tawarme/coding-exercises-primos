class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastpos = len(nums) - 1
        
        for i in range(len(nums) - 2, -1, -1):
            #print(lastpos)
            #print(i)
            if i + nums[i] >= lastpos:
                lastpos = i
        
        return lastpos == 0
