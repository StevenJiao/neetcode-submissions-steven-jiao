class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ret = ""
        if len(t) > len(s):
            return ret

        freqT = {}
        for c in t:
            freqT[c] = freqT.get(c, 0) + 1

        freqS = {}
        l = 0
        for r in range(len(s)):
            c = s[r]
            if c not in freqT and len(freqS) == 0:
                l += 1
            elif len(freqS) == 1 and c in freqS and freqS[c] == freqT[c]:
                l += 1
            else:
                freqS[c] = freqS.get(c, 0) + 1
                # print(freqS)

                if self.isSubstring(s, freqS, t, freqT):
                    ret = s[l:r + 1] if r - l + 1 < len(ret) or ret == "" else ret

                    freqS[s[l]] -= 1
                    if freqS[s[l]] == 0:
                        del freqS[s[l]]
                    l += 1
                    # print(freqS)
                    while l <= r and (s[l] not in freqT or freqT[s[l]] < freqS[s[l]]):
                        freqS[s[l]] -= 1
                        if freqS[s[l]] == 0:
                            del freqS[s[l]]
                        l += 1
                        # print(freqS)
                    if self.isSubstring(s, freqS, t, freqT):
                        ret = s[l:r+1] if r - l + 1 < len(ret) or ret == "" else ret
        return ret

    def isSubstring(self, s, freqS, t, freqT):
        isSubstring = True
        for char in freqT:
            if char not in freqS or freqS.get(char, 0) < freqT[char]:
                isSubstring = False
                break
        return isSubstring

