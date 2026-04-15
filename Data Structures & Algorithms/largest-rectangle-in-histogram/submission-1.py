class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stk = []
        for i in range(len(heights)):
            smallestIdx = i
            while stk and stk[-1][0] > heights[i]:
                prevHeight, idx = stk.pop()
                area = max(area, prevHeight * (i - idx))
                smallestIdx = idx

            stk.append((heights[i], smallestIdx))

        while stk:
            prevHeight, idx = stk.pop()
            area = max(area, prevHeight * (len(heights) - idx))

        return area