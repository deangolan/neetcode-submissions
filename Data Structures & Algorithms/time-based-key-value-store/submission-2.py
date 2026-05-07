class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store.setdefault(key, []).append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.store.get(key, [])

        l = 0
        r = len(vals) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            val, t = vals[m]
            if t <= timestamp:
                res = val
                l = m + 1
            else:
                r = m - 1

        return res

        
