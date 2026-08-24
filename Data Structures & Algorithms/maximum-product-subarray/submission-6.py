class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        currMax = 1
        currMin = 1
        for n in nums:
            if n == 0:
                currMax = 1
                currMin = 1
                continue
            temp = n * currMax
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(temp, n* currMin, n)
            ans = max(ans, currMax)

        return ans