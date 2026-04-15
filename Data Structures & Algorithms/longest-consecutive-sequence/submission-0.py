class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        setNums = set(nums)

        maxLength = 1
        for n in setNums:
            if n - 1 not in setNums:
                length = 1
                while n + length in setNums:
                    length += 1
                maxLength = max(maxLength, length)

        return maxLength