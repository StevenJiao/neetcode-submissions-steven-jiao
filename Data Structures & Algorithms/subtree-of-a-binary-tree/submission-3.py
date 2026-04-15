# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        q = deque([root])
        while q:
            curr = q.popleft()
            if self.isSameTree(curr, subRoot):
                return True
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return False
    
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        print("comparing: ", root.val, subRoot.val)
        q1 = deque([root])
        q2 = deque([subRoot])

        while q1 and q2:
            curr1 = q1.popleft()
            curr2 = q2.popleft()

            if (curr1.val if curr1 else None) != (curr2.val if curr2 else None):
                return False

            if curr1:
                q1.append(curr1.left)
                q1.append(curr1.right)

            if curr2:
                q2.append(curr2.left)
                q2.append(curr2.right)
    
        return len(q1) == len(q2)
