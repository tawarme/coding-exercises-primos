class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.search(nums, target, True)

        if first == -1:
            return [-1, -1]
        
        last = self.search(nums, target, False)

        return [first, last]

    def search(self, nums, target, is_first):
        left = 0
        right = len(nums) - 1

        while left <= right:
            #print(left, right)
            mid = int((left + right) / 2)

            if nums[mid] == target:
                #print(nums[mid], mid, "target found")

                if is_first:
                    if (left == mid or nums[mid-1] != target ):
                        return mid
                    else:
                        right = mid - 1
                else:
                    if (right == mid or nums[mid+1] != target ):
                        return mid
                    else:
                        left = mid + 1
            elif target < nums[mid]:
                #print("gone left")
                right = mid - 1
            else:
                left = mid + 1
                #print("HEEEEEEEEEEEEEELP")

        return -1
