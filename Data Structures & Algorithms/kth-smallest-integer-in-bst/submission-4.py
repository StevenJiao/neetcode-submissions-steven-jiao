# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 4
#3 5
#2
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        seen = set([None])
        inRes = set()
        res = []
        while stack:
            curr = stack[-1]
            if curr.left not in seen:
                stack.append(curr.left)
            else:
                if ((not res or curr.val != res[-1]) and (len(res) < 2 or curr.val != res[-2])):
                    res.append(curr.val)
                
                if curr.right not in seen:
                    stack.append(curr.right)
                else:
                    curr = stack.pop()
                    seen.add(curr)
        return res[k-1]
