class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seen = {len(s): True}
        
        def dfs(i: int) -> bool:
            if i in seen:
                return seen[i]
            for word in wordDict:
                if s.startswith(word, i) and dfs(i + len(word)):
                    seen[i] = True
                    return True
            seen[i] = False
            return False
        
        return dfs(0)