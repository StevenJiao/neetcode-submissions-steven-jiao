class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        ret = []
        perms = self.permute(nums[1::])
        for perm in perms:
            for i in range(len(perm)+1):
                p_copy = perm.copy()
                p_copy.insert(i, nums[0])
                ret.append(p_copy)
        return ret
