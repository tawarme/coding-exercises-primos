class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = {}
        for num in nums:
            if hashmap.get(num):
                return True
            else:
                hashmap[num] = True
