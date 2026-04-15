class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(idx: int, path: List[int]):
            if idx >= len(nums):
                ans.append(path.copy())
                return
            path.append(nums[idx])
            dfs(idx + 1, path)
            path.pop()
            dfs(idx + 1, path)
        dfs(0, [])
        return ans