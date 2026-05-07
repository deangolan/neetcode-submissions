class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rq = deque([])
        dq = deque([])
        for i, s in enumerate(senate):
            if s == 'R':
                rq.append(i)
            else:
                dq.append(i)

        while rq and dq:
            r = rq.popleft()
            d = dq.popleft()
            if r < d:
                rq.append(r + len(senate))
            else:
                dq.append(d + len(senate))
        
        if rq:
            return "Radiant"
        return "Dire"
