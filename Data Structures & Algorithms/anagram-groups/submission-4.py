class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def stringToFreqList(a: str):
            freq = {}
            for n in a:
                if n not in freq:
                    freq[n] = 1
                else:
                    freq[n] += 1
            return freq

        freqListStr = []

        for n in strs:
            freqListStr.append(stringToFreqList(n))

        done = set()
        ret = []

        for i, freqA in enumerate(freqListStr):
            if i in done:
                continue
            done.add(i)
            ret.append([strs[i]])
            for j, freqB in enumerate(freqListStr[(i+1):]):
                jIdx = j + i + 1
                if jIdx in done:
                    continue
                if freqA == freqB:
                    done.add(jIdx)
                    ret[-1].append(strs[jIdx])

        return ret
