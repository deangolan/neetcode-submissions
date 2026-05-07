class MedianFinder:

    def __init__(self):
        self.larger = []
        self.smaller = []

    def addNum(self, num: int) -> None:
        if len(self.larger) == 0:
            self.larger.append(num)
        elif num > self.larger[0]:
            heapq.heappush(self.larger, num)
        else:
            heapq.heappush(self.smaller, -num)
        if len(self.larger) - 1 > len(self.smaller):
            median = heapq.heappop(self.larger)
            heapq.heappush(self.smaller, -median)
        if len(self.smaller) > len(self.larger):
            median = heapq.heappop(self.smaller)
            heapq.heappush(self.larger, -median)

    def findMedian(self) -> float:
        print(self.larger, self.smaller)
        if (len(self.larger) + len(self.smaller)) % 2 == 0:
            return (self.larger[0] - self.smaller[0]) / 2

        return self.larger[0]