from functools import reduce
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minP, maxP = 1, max(piles)
        ret = maxP

        while minP <= maxP:
            mid = minP + (maxP - minP) // 2
            total = reduce(lambda x, p: x + math.ceil(p / mid), piles, 0)

            if (total <= h):
                ret = mid
                maxP = mid - 1
            else:
                minP = mid + 1
        return ret