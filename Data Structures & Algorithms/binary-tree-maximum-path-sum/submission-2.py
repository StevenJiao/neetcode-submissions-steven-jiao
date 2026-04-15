# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxes = {None: 0}
        stack = [root]
        res = float("-inf")
        while stack:
            curr = stack[-1]
            if curr.left not in maxes:
                stack.append(curr.left)
            elif curr.right not in maxes:
                stack.append(curr.right)
            else:
                curr = stack.pop()
                maxes[curr] = max(maxes[curr.left] + curr.val, maxes[curr.right] + curr.val, curr.val)
                res = max(res, maxes[curr], maxes[curr.left] + maxes[curr.right] + curr.val)

        return res