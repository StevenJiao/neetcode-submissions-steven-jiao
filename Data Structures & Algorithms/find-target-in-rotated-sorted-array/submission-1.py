class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if (nums[mid] == target):
                return mid
            # right side is not rotated
            elif (nums[mid] < nums[r]):
                # check if target is within this side
                if (nums[mid] < target and target <= nums[r]):
                    l = mid + 1
                # target is not, check left side
                else:
                    r = mid - 1
            # right side is rotated
            elif nums[mid] > nums[r]:
                # check if target is within left, un-rotated side
                if (nums[l] <= target and target < nums[mid]):
                    r = mid - 1
                # target is not, check right side
                else:
                    l = mid + 1

        return l if nums[l] == target else -1