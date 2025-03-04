"""
[0,30],[5,10],[15,20]

0, 5,  15
10, 20, 30


| ----- 0, 30  -------------|
  |--5,10----| |---15,20--|




"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        startTimes = sorted([startTime for startTime, endTime in intervals])
        endTimes = sorted([endTime for startTime, endTime in intervals])

        rooms = 0
        maxRooms = 0
        start = end = 0
        while start < len(intervals):
            if startTimes[start] < endTimes[end]:
                rooms += 1
                maxRooms = max(rooms, maxRooms)
                start += 1
            else:
                rooms -= 1
                end += 1
        return maxRooms

        