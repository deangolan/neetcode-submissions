class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = 0
        prepping = 0
        for arr, time in customers:
            prepping = max(arr, prepping) + time
            n += prepping - arr

        return (n / len(customers))
        