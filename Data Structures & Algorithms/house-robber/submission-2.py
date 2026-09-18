class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        a = nums[0]
        b = max(nums[1], nums[0])
        for i in range(2, n):
            best = max(a + nums[i], b)
            a = b
            b = best
        return max(a, b)




