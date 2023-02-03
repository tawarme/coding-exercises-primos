class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        if not intervals:
            return [newInterval]

        START = 0
        END = 1

        if intervals[-1][END] < newInterval[START]:
            intervals.append(newInterval)


        for i in range(len(intervals)):
            if intervals[i][END] < newInterval[START]:
                continue

            if intervals[i][START] > newInterval[START]:
                #break
                if intervals[i][START] > newInterval[END]:
                    intervals.insert(i, newInterval)
                    break

                intervals[i][START] = newInterval[START]

            if newInterval[END] <= intervals[i][END]:
                # Interval fully contained. Nothing to be done.
                break

            # New interval end is outside me
            # we can merge

            intervals[i][END] = newInterval[END]

            while i + 1 < len(intervals):
                if intervals[i+1][END] <= newInterval[END]:
                    del intervals[i+1]
                else:
                    if intervals[i+1][START] <= newInterval[END]:
                        intervals[i][1] = intervals[i+1][1]
                        del intervals[i+1]
                    break

            break



        return intervals
