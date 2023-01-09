class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        repetition = {}

        for num in nums:
            #print(repetition)
            if num in repetition:
                repetition[num] += 1
            else:
                repetition[num] = 1

            if repetition[num] > len(nums)/2:
                return num
