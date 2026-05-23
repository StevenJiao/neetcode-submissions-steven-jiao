class WordDictionary:

    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:
        curr = self.head
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        currCpy = self.head
        def backtrack(curr, idx) -> bool:
            if idx == len(word):
                return curr.isWord
            c = word[idx]

            if c == '.':
                for key in curr.children.keys():
                    if backtrack(curr.children[key], idx + 1):
                        return True
            
            if c not in curr.children:
                return False
            
            return backtrack(curr.children[c], idx + 1)

        return backtrack(currCpy, 0)


class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False