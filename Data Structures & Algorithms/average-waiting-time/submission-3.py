class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        time = 0
        prev = 0
        for i, t in customers:
            time += t
            if prev > i:
                time += prev-i
                prev += t
            else:
                prev = i+t
        return time/n
