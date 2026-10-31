class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_seen = {0: -1}
        prefix = 0
        longest = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                prefix -= 1
            else:
                prefix += 1
            if prefix in first_seen:
                length = i-first_seen[prefix]
                longest = max(longest, length)
            else:
                first_seen[prefix] = i
        return longest
            



















