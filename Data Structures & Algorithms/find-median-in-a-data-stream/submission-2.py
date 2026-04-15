class MedianFinder:

    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap

    def addNum(self, num: int) -> None:
        if self.small and num <= self.small[0]:
            heapq.heappush_max(self.small, num)
        else:
            heapq.heappush(self.large, num)

        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop_max(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush_max(self.small, val)

    def findMedian(self) -> float:
        if (len(self.small) > len(self.large)):
            return self.small[0]
        elif (len(self.small) < len(self.large)):
            return self.large[0]
        else:
            return (self.small[0] + self.large[0]) / 2
        
        