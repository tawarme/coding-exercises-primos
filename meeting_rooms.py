class Solution:
#    def meetingRooms(self, intervals: List[List[int]]):
    def meetingRooms(self, intervals):

        if len(intervals) <= 1:
            return True

        intervals.sort()

        prev = intervals[0]

        for cur in intervals[1:]:
            if prev[1] > cur[0]:
                return False

        return True


if __name__ == "__main__":
    tests = [
                [False, [[0, 30], [5, 10], [15, 20]]],
                [True, [[7, 10], [2, 4]]]
            ]

    for test in tests:
        ans = test[0]
        assert Solution().meetingRooms(*test[1:]) == ans
