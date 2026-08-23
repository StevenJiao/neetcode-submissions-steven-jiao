class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0:0}
        def dfs(currAmount: int) -> int:
            if currAmount in memo:
                return memo[currAmount]
            if currAmount == 0:
                return 0
            res = float("inf")
            for coin in coins:
                if currAmount - coin >= 0:
                    res = min(res, 1 + dfs(currAmount - coin))
            memo[currAmount] = res
            return res
        res = dfs(amount)
        return -1 if res == float("inf") else res