"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        endTimes = []
        for interval in intervals:
            if not endTimes:
                heapq.heappush(endTimes, interval.end)
                continue
            if interval.start < endTimes[0]:
                heapq.heappush(endTimes, interval.end)
            else:
                heapq.heappop(endTimes)
                heapq.heappush(endTimes, interval.end)

        return len(endTimes)

