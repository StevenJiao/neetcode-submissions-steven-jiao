class Solution:
    def rob(self, nums: List[int]) -> int:
        def robbing(arr: List[int]) -> int:
            rob1, rob2 = 0, 0

            for n in arr:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        robber1 = robbing(nums[1:])
        robber2 = robbing(nums[:-1])
        return max(robber1, robber2, nums[0])
