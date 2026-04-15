class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        if len(height) < 3:
            return total

        maxRHeights = []

        # for i, currHeight in enumerate(height):


        maxLHeight = height[0]
        for i, currHeight in enumerate(height):
            if (currHeight < maxLHeight):
                r = i + 1
                maxRHeight = 0

                if (r < len(height)):
                    maxRHeight = max(height[r:])
                
                if (currHeight < maxRHeight):
                    total += min(maxRHeight, maxLHeight) - currHeight

            if (currHeight > maxLHeight):
                maxLHeight = currHeight

        return total