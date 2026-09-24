class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = -1
        for pile in piles: #set right to max rate
            right = max(right, pile)
        minRate = right
        while left < right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += -(pile // -mid)
            if hours <= h: #go left
                minRate = min(minRate, mid)
                right = mid
            else: # go right
                left = mid + 1
        return minRate