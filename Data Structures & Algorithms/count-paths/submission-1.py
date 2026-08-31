class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        isPath = {(m,n): 1}
        def dfs(i,j) -> int:
            if (i,j) in isPath:
                return isPath[(i,j)]
            elif i > m or j > n:
                return 0
            path1 = dfs(i+1, j)
            if path1 != 0 and (i+1, j) not in isPath:
                isPath[(i+1,j)] = path1
            path2 = dfs(i,j+1)
            if path2 != 0 and (i,j+1) not in isPath:
                isPath[(i,j+1)] = path2
                
            return path1 + path2

        return dfs(1,1)