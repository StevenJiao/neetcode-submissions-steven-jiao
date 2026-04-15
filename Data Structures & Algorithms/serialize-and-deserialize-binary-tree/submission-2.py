# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        # q = deque([root])
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         res.append(str(node.val) if node else 'N')
        #         if node:
        #             q.append(node.left)
        #             q.append(node.right)

        def dfs(node: Optional[TreeNode]):
            if not node:
                res.append('N')
                return None
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(',')
        i = 1
        head = TreeNode(arr[0]) if arr[0] != 'N' else None

        # q = deque([head])
        # while q:
        #     curr = q.popleft()
        #     if not curr:
        #         break
        #     curr.left = TreeNode(arr[i]) if arr[i] != 'N' else None
        #     if curr.left:
        #         q.append(curr.left)
        #     i += 1
        #     curr.right = TreeNode(arr[i]) if arr[i] != 'N' else None
        #     if curr.right:
        #         q.append(curr.right)
        #     i += 1
        # return head

        self.i = 0
        def dfs():
            if arr[self.i] == 'N':
                self.i += 1
                return None

            node = TreeNode(arr[self.i])
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

