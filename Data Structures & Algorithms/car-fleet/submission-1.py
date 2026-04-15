class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedFleet = sorted(zip(position, speed), reverse=True)
        res = 0
        timeFleet = [(target - x[0]) / x[1] for x in sortedFleet]
        stk = []
        maxTime = -1
        for time in timeFleet:
            if maxTime == -1:
                # stk.append(time)
                res += 1
                maxTime = time
            elif time > maxTime:
                res += 1
                maxTime = time
        return res
