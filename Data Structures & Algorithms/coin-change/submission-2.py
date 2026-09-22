class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        dp[0] = 0
        for val in range(1, amount+1):
            minVal = float("inf")
            for coin in coins:
                prev = val-coin
                if prev >= 0:
                    minVal = min(minVal, dp[prev])
            dp[val] = minVal + 1
            print(val, minVal)
        if dp[amount] < float("inf"):
            return dp[amount]
        return -1