class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def backtrack(idx, path):
            if idx == len(nums):
                ans.append(path[:])
                return
            path.append(nums[idx])
            backtrack(idx+1, path)
            prevVal = path.pop()
            while idx + 1 < len(nums) and prevVal == nums[idx+1]:
                idx += 1
            backtrack(idx+1, path)
        backtrack(0, [])
        return ans
