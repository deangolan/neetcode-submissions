class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1]) # O(nlogn)
        dropOffs = []
        for trip in trips:
            passengers, frm, to = trip

            while dropOffs and dropOffs[0][0] <= frm:
                _, p = heapq.heappop(dropOffs)
                capacity += p

            heapq.heappush(dropOffs, (to, passengers))
                
            capacity -= passengers
            if capacity < 0:
                return False

        return True