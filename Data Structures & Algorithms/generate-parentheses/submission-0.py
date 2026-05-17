class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(curr: str, opens: int, pairs: int):
            if pairs == n:
                ans.append(curr)
                return
            # print(curr, opens, pairs)
            if opens + pairs < n:
                backtrack(curr + "(", opens + 1, pairs)
            if opens > 0:
                backtrack(curr + ")", opens - 1, pairs + 1)
        backtrack("", 0, 0)
        return ans