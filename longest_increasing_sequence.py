class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        lis = [1 for i in range(len(nums))]
        max_lenght = 1

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], 1+lis[j])
                    max_lenght = max(lis[i], max_lenght)
        return max_lenght
        """

        piles = [nums[0]]

        for i in range(1,len(nums)):
            if nums[i] > piles[-1]:
                piles.append(nums[i])
                continue

            left = 0
            right = len(piles) -1
            affected = 0
            while left < right:
                mid = int((left + right)/2)
                if piles[mid] == nums[i]:
                    affected = mid
                    break

                if piles[mid] < nums[i]:
                    left = mid +1
                else:
                    right = mid
            else:
                affected = left


            piles[affected] = nums[i]

            
        return len(piles)
