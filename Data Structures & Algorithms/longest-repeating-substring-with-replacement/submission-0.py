class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ret = 0
        dups = {}
        l = 0
        maxF = 0
        for r in range(len(s)):
            c = s[r]

            if c in dups.keys():
                dups[c] += 1
            else:
                dups[c] = 1

            for key in dups:
                maxF = max(dups[key], maxF)

            while r - l + 1 - maxF > k:
                dups[s[l]] -= 1
                if dups[s[l]] == 0:
                    dups.pop(s[l])
                l += 1

            ret = max(ret, r - l + 1)
            r += 1
        return ret