class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for word in words for c in word}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            # case for when we can't compare "when" with "whe"
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                c1, c2 = w1[j], w2[j]
                if c1 != c2:
                    # make c1 -> c2 connection
                    adj[c1].add(c2)
                    break
        visited = {}
        ans = []
        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visited[c] = False
            ans.append(c)
        for c in adj.keys():
            if dfs(c):
                return ""
        return "".join(ans[::-1])