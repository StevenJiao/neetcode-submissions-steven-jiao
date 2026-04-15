class MinStack:

    def __init__(self):
        self._stk=[]
        self._minStk = []

    def push(self, val: int) -> None:
        self._stk.append(val)
        minN = min(self.getMin(),val) if self._minStk else val
        self._minStk.append(minN)

    def pop(self) -> None:
        ret = self._stk.pop()
        self._minStk.pop()
        return ret

    def top(self) -> int:
        return self._stk[-1]

    def getMin(self) -> int:
        return self._minStk[-1]
