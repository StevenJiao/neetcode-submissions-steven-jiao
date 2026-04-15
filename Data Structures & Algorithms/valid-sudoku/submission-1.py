class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = [set() for i in range(9)]
        colSets = [set() for i in range(9)]
        sqSets = [[set() for i in range(3)] for j in range(3)]

        for i, row in enumerate(board):
            for j, n in enumerate(board[i]):
                if n == '.':
                    continue
                if n in rowSets[i]:
                    return False
                if n in colSets[j]:
                    return False
                if n in sqSets[i // 3][j // 3]:
                    return False

                rowSets[i].add(n)
                colSets[j].add(n)
                sqSets[i // 3][j // 3].add(n)

        return True