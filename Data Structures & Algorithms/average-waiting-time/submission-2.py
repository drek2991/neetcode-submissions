class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        time = 0
        prev = 0
        for i, t in customers:
            print(i, t, prev, time)
            time += t
            if prev > i:
                time += prev-i
                prev += t
            else:
                prev = i+t
        return time/n

# 1 2 0 0
# 2 5 3 2
# 4 3 8 8
# 10 1 11 15
# 12 2 12 17
# 13 4 26 19

