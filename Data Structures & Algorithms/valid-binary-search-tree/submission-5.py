# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, float("-inf"), float("inf"))]
        seen = set([None])
        while stack:
            curr, currMin, currMax = stack[-1]
            if curr.left not in seen:
                stack.append((curr.left, currMin, curr.val))
            elif curr.right not in seen:
                stack.append((curr.right, curr.val, currMax))
            else:
                curr, minVal, maxVal = stack.pop()
                if minVal >= curr.val or curr.val >= maxVal:
                    return False
                seen.add(curr)
        return True

