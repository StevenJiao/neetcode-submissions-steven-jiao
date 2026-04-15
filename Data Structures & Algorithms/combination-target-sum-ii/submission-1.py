class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def dfs(idx: int, subarr: List[int], currSum: int):
            if currSum == target:
                ans.append(subarr[:])
                return
            
            for j in range(idx, len(candidates)):
                if currSum + candidates[j] > target:
                    return
                if j > idx and candidates[j] == candidates[j - 1]:
                    continue
                
                subarr.append(candidates[j])
                currSum += candidates[j]

                dfs(j + 1, subarr, currSum)
                currSum -= subarr.pop()

        dfs(0, [], 0)

        return ans