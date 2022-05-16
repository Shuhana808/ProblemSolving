from typing import List
from icecream import ic


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        intervals = sorted(intervals, key=lambda element: (element[0], -element[1]))
        ic(intervals)
        count = len(intervals)
        max_second = intervals[0][1]
        for interval in intervals[1:]:
            first = interval[0]
            second = interval[1]
            ic(max_second)
            if second <= max_second:
                count -= 1
            else:
                max_second = second

        return count


c = Solution()
intervals =[[1,4],[2,3]]
ic(intervals)
res = c.removeCoveredIntervals(intervals)
ic(res)
