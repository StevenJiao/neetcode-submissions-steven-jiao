class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stk = []
        for i, t in enumerate(temperatures):
            if not stk or t <= stk[-1][0]:
                stk.append((t, i))
            else:
                while stk and t > stk[-1][0]:
                    j = stk.pop()[1]
                    ret[j] = i - j
                stk.append((t, i))
        return ret
            
                