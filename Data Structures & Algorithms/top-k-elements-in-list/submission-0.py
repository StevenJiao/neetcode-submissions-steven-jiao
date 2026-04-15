class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqList = {}

        for n in nums:
            if n not in freqList:
                freqList[n] = 0
            else:
                freqList[n] += 1
        
        sortedFreq = sorted(freqList.items(), key= lambda item: item[1], reverse=True)

        return [t[0] for t in sortedFreq[0:k]]

        