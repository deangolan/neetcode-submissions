class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freqs = {}
        for n in hand:
            freqs[n] = freqs.get(n, 0) + 1

        for n in sorted(hand):
            if freqs[n] <= 0:
                continue
            for m in range(groupSize):
                if freqs.get(n+m, -1) <= 0:
                    return False
                else:
                    freqs[n+m] -= 1
            
        return True