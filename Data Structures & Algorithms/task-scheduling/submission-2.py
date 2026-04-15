class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pq = []
        for task, freq in Counter(tasks).items():
            heapq.heappush_max(pq, [freq, task])

        res = 0
        q = deque([])
        while q or pq:
            if q and q[0][2] <= res:
                freq, task, time = q.popleft()
                heapq.heappush_max(pq, [freq, task])
            if pq:
                freq, task = heapq.heappop_max(pq)
                if freq - 1 > 0:
                    q.append([freq - 1, task, res + n + 1])
            else: 
                res = q[0][2] - 1
            res += 1

        return res