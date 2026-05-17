class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(arr: List[int], has: List[int]):
            if len(arr) == len(nums):
                ans.append(arr[:])
            for i in range(len(nums)):
                if not has[i]:
                    arr.append(nums[i])
                    has[i] = True
                    backtrack(arr, has)
                    has[i] = False
                    arr.pop()
        backtrack([], [False] * len(nums))
        return ans