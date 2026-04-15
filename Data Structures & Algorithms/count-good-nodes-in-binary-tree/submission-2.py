# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([(root, root.val if root else float("-inf"))])
        res = 0
        while q:
            curr, maxVal = q.popleft()
            newMax = max(maxVal, curr.val)
            if curr.val >= maxVal:
                res += 1
            if curr.left:
                q.append((curr.left, newMax))
            if curr.right:
                q.append((curr.right, newMax))
        return res
