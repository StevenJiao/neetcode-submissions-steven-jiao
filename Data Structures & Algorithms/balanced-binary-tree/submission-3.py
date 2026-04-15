# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stk = [root]
        heights = {None: 0}
        res = True
        while stk:
            curr = stk[-1]
            if curr.left not in heights:
                stk.append(curr.left)
            elif curr.right not in heights:
                stk.append(curr.right)
            else:
                curr = stk.pop()
                l_height = heights[curr.left] + (1 if curr.left else 0)
                r_height = heights[curr.right] + (1 if curr.right else 0)
                if abs(l_height - r_height) > 1:
                    return False
                    break
                
                heights[curr] = max(l_height, r_height)
        return res
