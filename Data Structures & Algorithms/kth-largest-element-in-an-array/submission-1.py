class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # pq = []
        # for num in nums:
        #     if len(pq) < k:
        #         heapq.heappush(pq, num)
        #         continue
            
        #     if num < pq[0]:
        #         continue
        #     else:
        #         heapq.heappush(pq, num)
        #         heapq.heappop(pq)
        # return pq[0]

        def quickSelect(l: int, r: int) -> int:
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if len(nums) - k < p:
                return quickSelect(l, p - 1)
            elif len(nums) - k > p:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)

