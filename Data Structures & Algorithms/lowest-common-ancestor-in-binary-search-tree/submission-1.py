# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]
        seen = { None: False }
        while stack:
            curr = stack[-1]

            if curr.left not in seen:
                stack.append(curr.left)
            elif curr.right not in seen:
                stack.append(curr.right)
            else:
                curr = stack.pop()
                left_or_right = seen[curr.right] or seen[curr.left]
                curr_is_child = curr.val == p.val or curr.val == q.val
                
                if (seen[curr.right] and seen[curr.left]) or (curr_is_child and (left_or_right)):
                    return curr
            
                seen[curr] = left_or_right or curr_is_child

        return None