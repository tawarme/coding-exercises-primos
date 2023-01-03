class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_dict = {}

        for i in range(len(nums)):
            num_dict[nums[i]] = i

        for i in range(len(nums)):
            numb = target - nums[i]
            if numb in num_dict and num_dict[numb] != i:
                return num_dict[numb], i
