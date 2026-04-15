class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a1, a2 = nums1, nums2
        if len(nums2) < len(nums1):
            a2 = nums1
            a1 = nums2
        l, r = 0, len(a1) - 1

        half = (len(a1) + len(a2)) // 2
        while True:
            mid1 = (l + r) // 2
            mid2 = half - (mid1 + 1) - 1
            a1Left = a1[mid1] if mid1 >= 0 else float('-inf')
            a1Right = a1[mid1 + 1] if (mid1 + 1) < len(a1) else float('inf')
            a2Left = a2[mid2] if mid2 >= 0 else float('-inf')
            a2Right = a2[mid2 + 1] if (mid2 + 1) < len(a2) else float('inf')

            if (a1Left <= a2Right and a1Right >= a2Left):
                print(a1Left, a1Right, a2Left, a2Right)
                if ((len(a1) + len(a2)) % 2 == 0):
                    return (max(a1Left, a2Left) + min(a1Right, a2Right)) / 2
                else:
                    return min(a1Right, a2Right)
            elif (a1Left > a2Right):
                r = mid1 - 1
            else:
                l = mid1 + 1
        return -1