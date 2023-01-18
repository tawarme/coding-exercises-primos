class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #[7, 0,1,2,4,5,6]
        #x = 0
        while len(nums) > 1:
            #x+=1
            #print(nums, nums[-1], nums[int(len(nums)/2)-1])
            #print(nums[int(len(nums)/2):], nums[:int(len(nums)/2)])
            if nums[0] <= nums[-1]:
                #print(x, "loops")
                return nums[0]

            nums = nums[int(len(nums)/2):] if nums[-1] < nums[int(len(nums)/2)-1] else nums[:int(len(nums)/2)]
            
        #print(x, "loops")

        return nums.pop()
