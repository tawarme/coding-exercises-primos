class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s_0 = 0
        s_1 = 0
        s_2 = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                del nums[i]
                nums.insert(s_0, 0)
                s_1 += 1
                s_2 += 1
            elif nums[i] == 1:
                del nums[i]
                nums.insert(s_1, 1)
                s_2 += 1
            else:
                del nums[i]
                nums.insert(s_2, 2)
