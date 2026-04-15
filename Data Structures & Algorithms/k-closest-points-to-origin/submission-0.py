class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for p in points:
            dist = math.dist(p, [0,0])
            pq.append((dist, p))
        heapq.heapify(pq)
        res = []
        for i in range(k):
            res.append(heapq.heappop(pq)[1])
        return res