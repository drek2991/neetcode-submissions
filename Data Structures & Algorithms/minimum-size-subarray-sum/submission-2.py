class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        left = 0
        right = 0
        sum = 0
        minLength = 100001
        while right < len(nums):
            sum += nums[right]
            while sum >= target:
                length = right-left+1
                minLength = min(length, minLength)
                sum -= nums[left]
                left += 1
            right += 1
        if minLength == 100001:
            return 0
        return minLength

