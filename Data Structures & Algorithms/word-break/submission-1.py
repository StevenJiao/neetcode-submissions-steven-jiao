class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seen = {'': True}
        
        def dfs(s: str) -> bool:
            if s in seen:
                return seen[s]
            for word in wordDict:
                if s.startswith(word) and dfs(s[len(word):]):
                    seen[s] = True
                    return True
            seen[s] = False
            return False
        
        return dfs(s)