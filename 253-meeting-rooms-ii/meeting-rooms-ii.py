"""
[0,30],[5,10],[15,20]

0, 5,  15
10, 20, 30


| ----- 0, 30  -------------|
  |--5,10----| |---15,20--|




"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        startTimes = sorted(intervals, key=lambda x:x[0])
        endTimes = sorted(intervals, key=lambda x:x[1])

        rooms = 0
        maxRooms = 0
        start = end = 0
        while start < len(intervals) and end < len(intervals):
            if startTimes[start][0] < endTimes[end][1]:
                rooms += 1
                start += 1
                maxRooms = max(rooms, maxRooms)
            else:
                rooms -= 1
                end += 1
        return maxRooms

        