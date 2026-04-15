class MedianFinder:

    def __init__(self):
        self.med1 = [] # max heap
        self.med2 = [] # min heap

    def addNum(self, num: int) -> None:
        if len(self.med1) == 0 or num <= self.med1[0] or (len(self.med2) > 0 and num < self.med2[0]):
            heapq.heappush_max(self.med1, num)
        else:
            heapq.heappush(self.med2, num)
        if abs(len(self.med1) - len(self.med2)) > 1:
            if (len(self.med1) > len(self.med2)):
                val = heapq.heappop_max(self.med1)
                heapq.heappush(self.med2, val)
            else:
                val = heapq.heappop(self.med2)
                heapq.heappush_max(self.med1, val)

    def findMedian(self) -> float:
        if (len(self.med1) > len(self.med2)):
            return self.med1[0]
        elif (len(self.med1) < len(self.med2)):
            return self.med2[0]
        else:
            return (self.med1[0] + self.med2[0]) / 2
        
        