class Solution:
    def climbStairs(self, n: int) -> int:
        a=1
        b=2
        for i in range(2, n):
            temp = a
            a = a+b
            b = b+temp
        if n%2==0: return b
        return a