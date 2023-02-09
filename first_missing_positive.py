class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        contains = 0

        # Verify if there is 1
        for i in range(len(nums)):
            if nums[i] == 1:
                contains += 1
                break

        # 1 not found,  1 is missing
        if contains:
            return 1

        # Convert all nums not in 1 .... n to 1
        for i in range(len(nums)):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = 1

        # Flip all nums "i" to negative
        for i in range(len(nums)):
            numabs = abs(num[i])
            
            # if numabs is last in possible F.M.P
            # then flip first element
            if numabs == n:
                nums[0] = -abs(nums[0])
            else:
                nums[numabs] = -abs(nums[numabs])


        # Return first found postive "i" th. If it was not flipped, then it
        # was missing
        for i in range(1, n):
            if nums[i] > 0:
                return i
        
        # If first element is positive then it was not flipped as n th cant be found in arr
        if nums[0] > n:
            return n

        # All previous passes worked, only missing next to last possible FMP
        return n + 1
