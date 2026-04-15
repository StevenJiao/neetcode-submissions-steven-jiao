class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ret = 1001
        while l <= r:
            mid = l + (r - l) // 2
            ret = min(ret, nums[mid])

            # right side not rotated
            if (nums[mid] < nums[r]):
                ret = min(ret, nums[mid])
                # check left side
                r = mid - 1
            # right side is rotated
            else:
                # get the min from the left, unrotated side
                ret = min(ret, nums[l])

                # check the right side
                l = mid + 1

        return ret