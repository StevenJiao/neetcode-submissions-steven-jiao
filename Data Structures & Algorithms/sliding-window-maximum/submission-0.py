class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        l, r = 0, k - 1

        while r < len(nums):
            max_in = max(nums[l:r+1])
            ret.append(max_in)
            r += 1
            l += 1
        return ret
