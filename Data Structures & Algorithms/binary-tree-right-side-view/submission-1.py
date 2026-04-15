# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        levels = []
        q = deque([root])
        while q:
            level = []
            for i in range(len(q)):
                curr = q.popleft()
                level.append(curr)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            levels.append(level)
        res = []
        print(levels)
        for level in levels:
            res.append(level[-1].val)
        return res