# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stk = [root]
        heights = {None: 0}
        res = 0
        while stk:
            curr = stk[-1]

            if curr.left not in heights:
                stk.append(curr.left)
            elif curr.right not in heights:
                stk.append(curr.right)
            else:
                curr = stk.pop()
                l_height = heights[curr.left]
                r_height = heights[curr.right]
                curr_dia = l_height + r_height
                res = max(res, curr_dia)

                heights[curr] = max(l_height, r_height) + 1
        return res