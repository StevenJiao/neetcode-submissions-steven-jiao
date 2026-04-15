class Solution:
    def isValid(self, s: str) -> bool:
        closeBrace = {')': '(', '}': '{', ']': '['}
        stk = []
        for c in list(s):
            if c in closeBrace:
                if not stk or stk.pop() != closeBrace[c]:
                    return False
            else:
                stk.append(c)
        return not stk