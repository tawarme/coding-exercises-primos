from heapq import *


class Solution:
    def meetingRoomsTwo(self, intervals):
        intervals.sort()

        heap = []

        max_rooms = 0

        for cur in intervals:
            while heap and heap[0] <= cur[0]:
                heappop(heap)

            heappush(heap, cur[1])

            max_rooms = max(max_rooms, len(heap))

        return max_rooms

    def meetingRoomsTwo2(self, intervals):
        starts = [interval[0] for interval in intervals]
        starts.sort()

        ends = [interval[1] for interval in intervals]
        ends.sort()

        end_i = 0
        count = 0

        for start in starts:
            if start >= ends[end_i]:
                end_i += 1

                # liberate space
                count -= 1

            # get more space
            count += 1
        
        return count


if __name__ == "__main__":
    tests = [
                [2, [[0, 30], [5, 10], [15, 20]]],
                [1, [[7, 10], [2, 4]]],
                [3, [[0, 30], [5, 10], [7, 20], [16, 34], [32, 40]]]
            ]

    for test in tests:
        ans = test[0]
        dat = Solution().meetingRoomsTwo2(*test[1:])
        try:
            assert dat == ans
        except:
            print(f"Print ERROR, expected: {ans} got {dat}")
