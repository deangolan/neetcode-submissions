class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end = intervals[0][1]

        count = 0
        for l, r in intervals[1:]:
            if l >= end:
                end = r
            else:
                count += 1
                end = min(end, r)
        return count 