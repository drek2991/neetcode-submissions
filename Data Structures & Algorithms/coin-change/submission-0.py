class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        dp[0] = 0
        for val in range(1, amount+1):
            minVal = 100000
            for coin in coins:
                prev = val-coin
                if prev >= 0 and prev in dp:
                    minVal = min(minVal, dp[prev])
            dp[val] = minVal + 1
            print(val, minVal)
        if dp[amount] < 100000:
            return dp[amount]
        return -1



                