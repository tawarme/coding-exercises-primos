class Solution(object):
    """
    #def explore(self, numval, dir, hashmap, explored):
    def explore(self, numval, dir, hashmap):
        #if explored.get(numval):
        #    return 0

        #explored[numval] = True
        
        if hashmap.get(numval):
            #return 1 + self.explore(numval+dir, dir, hashmap, explored)
            return 1 + self.explore(numval+dir, dir, hashmap)
        
        return 0
    """


    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}

        for num in nums:
            hashmap[num] = True

        #explored = {}

        max_len = 0

        """
        for i in range(len(nums)):
            #if explored.get(nums[i]):
            #    continue
            #explored[nums[i]] = True

            seq_len_l = self.explore(nums[i] +1, + 1, hashmap)
            #seq_len_l = self.explore(nums[i] +1, + 1, hashmap, explored)
            seq_len_r = self.explore(nums[i] -1, - 1, hashmap)
            #seq_len_r = self.explore(nums[i] -1, - 1, hashmap, explored)
            max_len = max(max_len, 1+seq_len_l+seq_len_r)

            if max_len > len(nums)/2:
                break

        """

        for numval in hashmap:
            if hashmap.get(numval-1):
                continue

            cur_len = 1

            while hashmap.get(numval + cur_len) is not None:
                cur_len += 1

            max_len = max(max_len, cur_len)

        return max_len