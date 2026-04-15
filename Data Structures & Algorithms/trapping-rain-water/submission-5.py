class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        if len(height) < 3:
            return total

        maxRHeights = [-1] * len(height)
        maxRHeight = height[-1]
        for i, currHeight in enumerate(reversed(height)):
            if (currHeight > maxRHeight):
                maxRHeight = currHeight

            maxRHeights[len(height) - i - 1] = maxRHeight

        maxLHeight = height[0]
        for i, currHeight in enumerate(height):
            if (currHeight < maxLHeight):
                maxRHeight = maxRHeights[i]
                
                if (currHeight < maxRHeight):
                    total += min(maxRHeight, maxLHeight) - currHeight

            if (currHeight > maxLHeight):
                maxLHeight = currHeight

        return total