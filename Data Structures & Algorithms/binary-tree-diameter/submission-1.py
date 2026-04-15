# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0

        q = deque()
        q.append(root)
        while q:
            curr = q.popleft()

            maxLeft = self.maxDepth(curr.left)
            maxRight = self.maxDepth(curr.right)
            res = max(res, maxLeft + maxRight)
            if curr.left and curr.right and maxLeft == maxRight:
                q.append(curr.left)
                q.append(curr.right)
            elif curr.left and maxLeft > maxRight:
                q.append(curr.left)
            elif curr.right and maxRight > maxLeft:
                q.append(curr.right)

        return res
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
        
