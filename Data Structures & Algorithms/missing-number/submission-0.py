class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        exp = 0
        tot = 0
        for i in range(len(nums)):
            exp += i
            tot += nums[i]
        exp += len(nums)
        return exp-tot