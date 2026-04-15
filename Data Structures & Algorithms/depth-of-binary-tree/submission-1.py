# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        return self.dfs(root, res)
    
    def dfs(self, root: Optional[TreeNode], res) -> int:
        if not root:
            return res
        
        res += 1
        maxL = self.dfs(root.left, res)
        maxR = self.dfs(root.right, res)
        return max(maxL, maxR)