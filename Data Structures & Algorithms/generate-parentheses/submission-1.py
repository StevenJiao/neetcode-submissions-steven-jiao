class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(curr: str, opens: int, closes: int):
            if closes == n:
                ans.append(curr)
                return

            if closes < n and opens < n:
                backtrack(curr + "(", opens + 1, closes)
            if opens > closes:
                backtrack(curr + ")", opens, closes + 1)
        backtrack("", 0, 0)
        return ans