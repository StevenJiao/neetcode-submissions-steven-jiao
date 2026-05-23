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
        def dfs(curr, idx) -> bool:

            for i in range(idx, len(word)):
                c = word[i]
                if c == '.':
                    for key in curr.children.keys():
                        if dfs(curr.children[key], i + 1):
                            return True
                    return False
                elif c not in curr.children:
                    return False
                else:
                    curr = curr.children[c]

            return curr.isWord

        return dfs(currCpy, 0)


class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False