import math

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_weight = max(weights)
        l = max_weight
        r = max_weight * math.ceil(len(weights) / days)

        res = r
        while l <= r:
            cap = (l + r) // 2

            rem = cap
            days_needed = 1
            for w in weights:
                if w > rem: 
                    # print("need extra day from weight:", w)
                    days_needed += 1
                    rem = cap - w
                else:
                    rem -= w
            # print("days needed:", days, "with capacity:", cap)
            
            if days_needed <= days:
                res = cap
                r = cap - 1
            else:
                l = cap + 1

        return res

        