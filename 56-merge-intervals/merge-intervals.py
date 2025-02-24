class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedIntervals = sorted(intervals, key=lambda x:x[0])
        res = [sortedIntervals[0]]
        for start, end in sortedIntervals[1:]:
            prevStart, prevEnd = res[-1]

            # case 1: partial overlap
            if prevEnd >= start:
                res[-1][1] = max(end, prevEnd)
            # case 3: no overlap
            else:
                res.append([start, end])
        return res

            




        