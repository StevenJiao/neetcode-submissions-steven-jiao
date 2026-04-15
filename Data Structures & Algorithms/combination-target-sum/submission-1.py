class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        def dfs(idx: int, subset: List[int], subsetSum: int):
            if subsetSum == target:
                ans.append(subset[:])
                return

            for j in range(idx, len(nums)):
                if nums[j] + subsetSum > target:
                    return
                subsetSum += nums[j]
                subset.append(nums[j])
                dfs(j, subset, subsetSum)
                subsetSum -= subset.pop()
        
        dfs(0, [], 0)
        return ans