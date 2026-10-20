class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 1
        sum = 0
        if len(nums) > 0:
            sum += nums[left]
        minLength = 100001
        while right < len(nums):
            print(left, right, sum)
            if sum >= target:
                length = right-left
                if length < minLength:
                    minLength = length
                sum -= nums[left]
                left += 1
            else:
                sum += nums[right]
                right += 1
        if minLength == 100001:
            return 0
        return minLength

