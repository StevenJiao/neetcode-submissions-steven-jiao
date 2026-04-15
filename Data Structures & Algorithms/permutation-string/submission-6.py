class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False
        freqs1 = {}
        freqs2 = {}

        for i in range(len(s1)):
            freqs1[s1[i]] = 1 + freqs1.get(s1[i], 0)
            freqs2[s2[i]] = 1 + freqs2.get(s2[i], 0)
        
        l = 0

        for r in range(len(s1), len(s2)):

            if freqs1 == freqs2:
                return True

            c = s2[r]
            freqs2[c] = 1 + freqs2.get(c, 0)
            c=s2[l]
            freqs2[c] = freqs2.get(c) - 1

            if freqs2[c] == 0:
                del freqs2[c]
            l += 1

        return freqs1 == freqs2