# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [root]
        seen = set([None])
        inRes = set()
        res = []
        while stack:
            curr = stack[-1]
            if not curr.left and not curr.right:
                inRes.add(curr)
                res.append(curr.val)
            if curr.left not in seen:
                stack.append(curr.left)
            else:
                if curr not in inRes:
                    res.append(curr.val)
                    inRes.add(curr)
                if curr.right not in seen:
                    stack.append(curr.right)
                else:
                    curr = stack.pop()
                    seen.add(curr)

        print(res)
        for i in range(len(res)-1):
            if res[i] >= res[i+1]:
                return False
        return True