class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {len(nums)-1:nums[-1]}
        
        def dfs(i: int) -> int:
            if i in memo:
                return memo[i]

            memo[i] = max(nums[i], nums[i] + dfs(i+1))
                
            return memo[i]

        ans = float("-inf")
        for i in range(len(nums)):
            ans = max(ans, dfs(i))
        return ans
            