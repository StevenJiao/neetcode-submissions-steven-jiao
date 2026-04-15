import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        l, r = 0, 0
        q = []

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if (q[0] < l):
                q.pop(0)

            if r + 1 >= k:
                ret.append(nums[q[0]])
                l += 1
            r += 1

        return ret
