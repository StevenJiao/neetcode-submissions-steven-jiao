class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s): 
            return 0
        l, r = 0, 1
        longest_s = [s[0]]
        dup = { s[0] : 1 }
        longest = 1

        while r < len(s):
            c = s[r]
            if dup.get(c, 0) > 0:
                while (longest_s) and dup.get(c, 0) > 0:
                    frontC = longest_s.pop(0)
                    dup[frontC] = 0

            dup[c] = 1
            longest_s.append(c)
            longest = max(longest, len(longest_s))
            r += 1

        return longest