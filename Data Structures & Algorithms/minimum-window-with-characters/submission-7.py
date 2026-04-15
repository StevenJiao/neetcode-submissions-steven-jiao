class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        freqT, window = {}, {}
        for c in t:
            freqT[c] = freqT.get(c, 0) + 1

        l = 0
        have = 0
        res, resLen = [-1, -1], float("inf")
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            # have we found what we need for the substring? 
            if window[c] == freqT.get(c, 0):
                have += 1

            # yes, we have. Now we try and cut off things from the left side until we don't 
            while have == len(freqT):

                # store minimum as we go
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # cut the left side until we don't have what we need
                window[s[l]] -= 1
                if (s[l] in freqT and window[s[l]] < freqT[s[l]]):
                    have -= 1
                l += 1

        # get the resultant substring
        return s[res[0]:res[1]+1] if resLen != float("inf") else ""