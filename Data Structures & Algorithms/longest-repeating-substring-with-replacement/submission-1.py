class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ret = 0
        count = {}
        l = 0
        maxF = 0
        for r in range(len(s)):
            c = s[r]

            if c in count.keys():
                count[c] += 1
            else:
                count[c] = 1

            for key in count:
                maxF = max(count[key], maxF)

            while r - l + 1 - maxF > k:
                count[s[l]] -= 1
                l += 1

            ret = max(ret, r - l + 1)
        return ret