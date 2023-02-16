class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        #queue = []
        queue = deque()

        maxes = []
        for i in range(len(nums)):
            while queue and queue[0] <= i - k:
                #queue.pop(0)
                queue.popleft()

            while queue and nums[queue[-1]] < nums[i]:
                #queue.pop(-1)
                queue.pop()

            queue.append(i)

            maxes.append(nums[queue[0]])


        return maxes[k-1:]
