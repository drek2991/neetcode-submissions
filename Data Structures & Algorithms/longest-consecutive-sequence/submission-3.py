class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        nums.sort()
        ans = 1
        curr = 1
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                curr += 1
                ans = max(ans, curr)
            elif nums[i] < nums[i+1]:
                curr = 1
            else:
                continue
        return ans