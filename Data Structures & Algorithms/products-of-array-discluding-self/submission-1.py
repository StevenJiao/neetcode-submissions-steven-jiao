class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = [0] * len(nums)
        # suffix = [0] * len(nums)
        ans = [1] * len(nums)
        # for i in range(len(nums)):
        #     if i == 0:
        #         prefix[i] = nums[i]
        #     else:
        #         prefix[i] = prefix[i - 1] * nums[i]

        # for i in range(len(nums) - 1, 0, -1):
        #     if i == (len(nums)) - 1:
        #         suffix[i] = nums[i]
        #     else:
        #         suffix[i] = nums[i] * suffix[i + 1]
        prefix = 1
        for i in range(len(nums)):
            ans[i] *= prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
        
        # for i in range()

        return ans