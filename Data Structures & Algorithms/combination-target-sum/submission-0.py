class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        def dfs(idx: int, subset: List[int], subsetSum: int):
            if subsetSum == target:
                ans.append(subset[:])
                return
            if idx >= len(nums) or subsetSum > target:
                return

            subsetSum += nums[idx]
            subset.append(nums[idx])

            dfs(idx, subset, subsetSum)
            subsetSum -= subset.pop() if subset else 0
            dfs(idx + 1, subset, subsetSum)
        
        dfs(0, [], 0)
        return ans