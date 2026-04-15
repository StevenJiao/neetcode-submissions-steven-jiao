# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ''
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                res += f"/{node.val if node else '*'}|"
                if node:
                    q.append(node.left)
                    q.append(node.right)
            res += '#'

        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = []
        for i in range(len(data)):
            numStr = ''
            if data[i] == '/':
                i += 1
                while data[i] != '|':
                    numStr += data[i]
                    i += 1
                arr.append(int(numStr) if numStr != '*' else None)
        
        head = TreeNode(arr[0]) if arr[0] else None
        q = deque([head])
        for i in range(1, len(arr), 2):
            if not q:
                break

            curr = q.popleft()
            if not curr:
                break
            curr.left = TreeNode(arr[i]) if arr[i] else None
            curr.right = TreeNode(arr[i+1]) if arr[i+1] else None
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        return head



