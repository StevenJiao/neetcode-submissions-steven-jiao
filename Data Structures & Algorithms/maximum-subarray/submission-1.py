class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {(len(nums)-1, True):nums[-1],(len(nums)-1, False):nums[-1]}
        
        def dfs(i: int, isContinuous: bool = True) -> int:
            if (i, isContinuous) in memo:
                return memo[(i,isContinuous)]

            continuousArr = max(nums[i], nums[i] + dfs(i+1))
            if isContinuous:
                memo[(i,isContinuous)] = continuousArr
                return memo[(i,isContinuous)]
            else:
                nonContinuousArr = max(continuousArr, dfs(i+1, False))
                memo[(i,isContinuous)] = nonContinuousArr
                
            return memo[(i,isContinuous)]
        return dfs(0, False)
            