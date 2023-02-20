class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        START = 0
        END = 1
        i = 0

        while i < len(intervals) - 1:
            cur = intervals[i]
            next = intervals[i + 1]

            if next[START] <= cur[END]:
                if next[END] <= cur[END]:
                    del intervals[i + 1]
                else:
                    cur[END] = next[END]
            else:
                i += 1

        return intervals
