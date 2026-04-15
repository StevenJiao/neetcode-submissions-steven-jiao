class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        if len(height) < 3:
            return total

        maxLHeight = height[0]
        for i, currHeight in enumerate(height):
            if (currHeight < maxLHeight):
                r = i
                maxRHeight = 0

                while (r < len(height)):
                    if (height[r] > maxRHeight):
                        maxRHeight = height[r]
                    r += 1
                
                if (currHeight < maxRHeight):
                    total += min(maxRHeight, maxLHeight) - currHeight

            if (currHeight > maxLHeight):
                maxLHeight = currHeight

        return total