"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        deltas = []
        for interval in intervals:
            deltas.append((interval.start, 1))
            deltas.append((interval.end, -1))
        deltas.sort()
        minRooms = 0
        curr = 0
        for time, delta in deltas:
            curr += delta
            minRooms = max(minRooms, curr)
        return minRooms

