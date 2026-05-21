class PrefixTree:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        curr = self.head
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.head
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        print(curr.children)
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True
        
class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False