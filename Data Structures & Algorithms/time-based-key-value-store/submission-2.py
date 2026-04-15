class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map.keys():
            self.map[key] = [(value, timestamp)]
        else:
            arr = self.map.get(key)
            arr.append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.map.get(key, [])
        l, r = 0, len(arr) - 1
        ret = ""

        while l <= r:
            mid = l + (r - l) // 2

            if (arr[mid][1] == timestamp):
                return arr[mid][0]
            elif (timestamp > arr[mid][1]):
                ret = arr[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return ret