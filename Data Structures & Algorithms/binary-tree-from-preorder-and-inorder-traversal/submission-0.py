# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexes = {val: ind for ind, val in enumerate(inorder)}
        self.pre_idx = 0
        def dfs(l, r):
            if l > r:
                return None

            head = TreeNode(preorder[self.pre_idx])
            self.pre_idx += 1
            mid = indexes[head.val]

            head.left = dfs(l, mid - 1)
            head.right = dfs(mid + 1, r)
            return head

        return dfs(0, len(inorder)-1)
        
