class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        maxRows = len(heights)
        maxCols = len(heights[0])

        def dfs(i,j,prevVal,setToAddTo):
            if i < 0 or i >= maxRows or j < 0 or j >= maxCols or (i,j) in setToAddTo or heights[i][j] < prevVal:
                return
            val = heights[i][j]

            setToAddTo.add((i,j))
            dfs(i+1,j,val,setToAddTo)
            dfs(i,j+1,val,setToAddTo)
            dfs(i-1,j,val,setToAddTo)
            dfs(i,j-1,val,setToAddTo)

        # traverse top and bottom
        for j in range(maxCols):
            dfs(0,j,heights[0][j],pacific)
            dfs(maxRows-1,j,heights[maxRows-1][j],atlantic)
        
        # traverse left and right
        for i in range(maxRows):
            dfs(i,0,heights[i][0],pacific)
            dfs(i,maxCols-1,heights[i][maxCols-1],atlantic)
        return [[i,j] for i,j in pacific if (i,j) in atlantic]