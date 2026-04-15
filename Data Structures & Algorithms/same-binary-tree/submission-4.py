# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_queue = deque([p])
        q_queue = deque([q])
        while p_queue and q_queue:
            if len(p_queue) != len(q_queue):
                return False
            for i in range(len(p_queue)):
                curr_p = p_queue.popleft()
                curr_q = q_queue.popleft()
                isCurrEqual = (curr_p.val if curr_p else None) == (curr_q.val if curr_q else None)
                isLeftEqual = (curr_p.left.val if curr_p and curr_p.left else None) == (curr_q.left.val if curr_q and curr_q.left else None)
                isRightEqual = (curr_p.right.val if curr_p and curr_p.right else None) == (curr_q.right.val if curr_q and curr_q.right else None)
                if not isCurrEqual or not isLeftEqual or not isRightEqual:
                    return False
                if curr_p and curr_p.left:
                    p_queue.append(curr_p.left)
                if curr_p and curr_p.right:
                    p_queue.append(curr_p.right)
                if curr_q and curr_q.left:
                    q_queue.append(curr_q.left)
                if curr_q and curr_q.right:
                    q_queue.append(curr_q.right)
        return len(p_queue) == len(q_queue)
