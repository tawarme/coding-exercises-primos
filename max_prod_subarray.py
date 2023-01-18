class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        cur = 1
        mini = nums[0]
        maxi = nums[0]
        result = maxi
        
        for num in nums[1:]:
            cur = num
            temp = max(cur, max(mini*cur, maxi*cur))
            mini = min(cur, min(mini*cur, maxi*cur))
            maxi = temp

            result = max(result, maxi)

        return result
