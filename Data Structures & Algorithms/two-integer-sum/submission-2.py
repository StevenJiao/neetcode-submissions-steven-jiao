class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            val = nums[i]
            needVal = target - val

            if needVal in seen:
                return [seen[needVal], i]

            if val not in seen:
                seen[val] = i
        return []