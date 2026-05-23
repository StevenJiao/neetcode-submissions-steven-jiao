class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        head = Node()

        for word in words:
            curr = head
            for c in word:
                if c not in curr.children:
                    curr.children[c] = Node()
                curr = curr.children[c]
            curr.isWord = True

        ans = []
        def dfs(curr, i, j, word):
            if curr.isWord:
                ans.append(word)
                curr.isWord = False
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or board[i][j] not in curr.children:
                return
            c = board[i][j]
            board[i][j] = '*'
            dfs(curr.children[c],i+1,j,word+c)
            dfs(curr.children[c],i,j+1,word+c)
            dfs(curr.children[c],i-1,j,word+c)
            dfs(curr.children[c],i,j-1,word+c)
            board[i][j] = c
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                currCpy = head
                dfs(currCpy, i, j,"")
        return ans

class Node: 
    def __init__(self):
        self.children = {}
        self.isWord = False