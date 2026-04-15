class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        ans = [0] * len(nums)
        deb = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i - 1] * nums[i]

        for i in range(len(nums) - 1, 0, -1):
            if i == (len(nums)) - 1:
                suffix[i] = nums[i]
            else:
                suffix[i] = nums[i] * suffix[i + 1]

        for i in range(len(nums)):
            num1 = prefix[i - 1] if i - 1 >= 0 else 1
            num2 = suffix[i + 1] if i + 1 <= len(nums) - 1 else 1
            ans[i] = num1 * num2

        return ans