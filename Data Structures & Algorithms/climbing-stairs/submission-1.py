class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(currNum: int, seen: {int: int}):
            if currNum == n:
                return 1
            elif currNum > n:
                return 0

            nextNum1 = currNum + 1
            nextNum2 = currNum + 2
            count1 = seen[nextNum1] if nextNum1 in seen else dfs(currNum + 1, seen)
            count2 = seen[nextNum2] if nextNum2 in seen else dfs(currNum + 2, seen)
            seen[nextNum1] = count1
            seen[nextNum2] = count2
            return count1 + count2
        
        return dfs(0, {})