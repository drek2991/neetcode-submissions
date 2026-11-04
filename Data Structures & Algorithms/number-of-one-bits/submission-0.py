class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 1:
            ans += 1
            n //= 2
        return ans