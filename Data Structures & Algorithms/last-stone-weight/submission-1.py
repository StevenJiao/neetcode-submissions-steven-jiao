class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = stones
        heapq.heapify_max(pq)
        while len(pq) > 1:
            s1 = heapq.heappop_max(pq)
            s2 = heapq.heappop_max(pq)
            diff = abs(s1 - s2)
            if diff:
                heapq.heappush_max(pq, diff)
            
        return pq[0] if len(pq) else 0