class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        while len(tickets) > 0:
            val = tickets.pop(0)
            if k == 0:
                if val == 1:
                    return time+1
                else:
                    tickets.append(val-1)
                    k = len(tickets)
            else:
                if val != 1:
                    tickets.append(val-1)
            k -= 1
            time += 1
        return time