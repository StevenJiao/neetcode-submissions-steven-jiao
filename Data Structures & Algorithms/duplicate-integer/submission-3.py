class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = set();
        
        for i in range(len(nums)):
            if nums[i] in dups:
                return True
            dups.add(nums[i])

        return False
