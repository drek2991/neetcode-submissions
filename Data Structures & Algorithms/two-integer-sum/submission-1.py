class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in comp:
                return [comp[complement], i]
            else:
                comp[nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in comp:
                return [i, comp[nums[i]]]
