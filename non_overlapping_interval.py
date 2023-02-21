class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()

        prev = 0
        count = 0
        START = 0
        END = 1
        for i in range(1, len(intervals)):
            if intervals[prev][END] > intervals[i][START]:
                if intervals[prev][END] > intervals[i][END]:
                    prev = i
                count += 1
            else:
                prev = i

        return count
