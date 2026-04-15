class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqs1 = {}
        freqs2 = {}
        for c in s1:
            freqs1[c] = 1 + freqs1.get(c, 0)
        l = 0

        for r in range(len(s2)):
            c = s2[r]

            if c not in freqs1.keys():
                l = r
                freqs2 = {}
            else:
                if len(freqs2) == 0:
                    l = r

                freqs2[c] = 1 + freqs2.get(c, 0)

                if freqs1 == freqs2:
                    return True

                while freqs1.get(c) < freqs2.get(c):
                    freqs2[s2[l]] = freqs2[s2[l]] - 1
                    l+=1
    
        return False