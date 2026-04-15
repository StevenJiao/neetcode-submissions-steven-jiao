"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        maxRooms = 0
        meetingEnds=[]
        for interval in intervals:
            if meetingEnds and interval.start >= meetingEnds[0]:
                heapq.heappop(meetingEnds)
            heapq.heappush(meetingEnds, interval.end)
            maxRooms = max(len(meetingEnds), maxRooms)
        return maxRooms
