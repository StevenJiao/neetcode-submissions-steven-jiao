class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ops = set(['+', '-', '*', '/'])
        for token in tokens:
            if token == '+':
                stk.append(stk.pop() + stk.pop())
            elif token == '-':
                val1, val2 = stk.pop(), stk.pop()
                stk.append(val2 - val1)
            elif token == '*':
                stk.append(stk.pop() * stk.pop())
            elif token == '/':
                val1, val2 = stk.pop(), stk.pop()
                stk.append(int(val2 / val1))
            else:
                stk.append(int(token))
        return stk.pop()
