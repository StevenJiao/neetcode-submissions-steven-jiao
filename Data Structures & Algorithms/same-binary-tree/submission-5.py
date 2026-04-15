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
                if (curr_p.val if curr_p else None) != (curr_q.val if curr_q else None):
                    return False
                if curr_p:
                    p_queue.append(curr_p.left)
                    p_queue.append(curr_p.right)
                if curr_q:
                    q_queue.append(curr_q.left)
                    q_queue.append(curr_q.right)
        return len(p_queue) == len(q_queue)
