class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        right = 0
        mid = int(len(nums) / 2)
        left = len(nums) - 1

        while right != mid and mid != left:
            print(right, mid, left)
            if nums[left] == target:
                return left

            if nums[right] == target:
                return right

            if nums[right] < nums[mid]:
                #print("right is ordered")
                if nums[right] < target < nums[mid]:
                    left = mid
                else:
                    right = mid
            else:
                #print("left is ordered")
                if nums[mid] < target < nums[left]:
                    right = mid
                else:
                    left = mid
            mid = int((right + left) / 2)

        if nums[left] == target:
            return left

        if nums[right] == target:
            return right
        
        return -1
