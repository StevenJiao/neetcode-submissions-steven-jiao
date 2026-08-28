class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [-1] * len(nums)
        def dfs(i: int) -> int:
            if i == len(nums):
                return 1
            if LIS[i] != -1:
                return LIS[i]
            maxLIS = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    maxLIS = max(maxLIS, 1 + dfs(j))
            LIS[i] = maxLIS
            return maxLIS

        return max(dfs(i) for i in range(len(nums)))