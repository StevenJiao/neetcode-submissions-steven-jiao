class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            if len(pq) < k:
                heapq.heappush(pq, num)
                continue
            
            if num < pq[0]:
                continue
            else:
                heapq.heappush(pq, num)
                heapq.heappop(pq)
        return pq[0]