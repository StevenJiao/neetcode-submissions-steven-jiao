class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        if not height:
            return total

        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        while (l < r):
            if (maxL < maxR):
                l += 1
                maxL = max(maxL, height[l])
                total += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                total += maxR - height[r]

        return total