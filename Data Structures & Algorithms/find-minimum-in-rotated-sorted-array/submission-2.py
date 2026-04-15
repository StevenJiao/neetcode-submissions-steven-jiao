class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ret = 1001
        while l <= r:
            mid = l + (r - l) // 2
            ret = min(ret, nums[mid])

            # right side not rotated, answer is in left side
            if (nums[mid] < nums[r]):
                r = mid - 1
            # right side is rotated, answer is in right side
            else:
                # check the right side
                l = mid + 1

        return ret