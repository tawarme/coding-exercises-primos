class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #print(nums)
        ans = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            right = i + 1
            left = len(nums) - 1
            target = 0 - nums[i]

            while right < left:
                #print(target, nums[left], nums[right])
                sum = nums[left] + nums[right]

                if sum > target:
                    left -= 1
                elif sum < target:
                    right += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left -= 1
                    right += 1
                    while right < left and nums[right] == nums[right - 1]:
                        right += 1

        return ans
