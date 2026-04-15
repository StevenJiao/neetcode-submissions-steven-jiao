# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        maxes = {None: float("-inf")}
        seen = set([None])
        stack = [root]
        curr_max = root.val
        res = 0
        while stack:
            curr = stack[-1]
            curr_max = max(curr_max, curr.val) if curr not in maxes else maxes[curr]
            maxes[curr] = curr_max
            if curr.left not in seen:
                stack.append(curr.left)
            elif curr.right not in seen:
                stack.append(curr.right)
            else:
                curr = stack.pop()
                if curr.val >= maxes[curr]:
                    res += 1
                seen.add(curr)
        return res

