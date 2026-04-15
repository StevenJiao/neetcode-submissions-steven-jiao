class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def dfs(idx: int, subarr: List[int], currSum: int):
            if currSum == target:
                ans.append(subarr[:])
                return
            if idx == len(candidates) or currSum > target:
                return
            
            subarr.append(candidates[idx])
            currSum += candidates[idx]

            dfs(idx + 1, subarr, currSum)
            currSum -= subarr.pop()

            while idx + 1 < len(candidates) and candidates[idx + 1] == candidates[idx]:
                idx += 1
            dfs(idx + 1, subarr, currSum)

        dfs(0, [], 0)

        return ans