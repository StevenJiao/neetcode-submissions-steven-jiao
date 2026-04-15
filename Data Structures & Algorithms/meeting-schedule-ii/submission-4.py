"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        times = []
        for interval in intervals:
            times.append((interval.start, 1))
            times.append((interval.end, -1))

        times.sort()
        rooms = 0
        maxRooms = 0
        for time, delta in times:
            rooms += delta
            maxRooms = max(maxRooms, rooms)

        return maxRooms