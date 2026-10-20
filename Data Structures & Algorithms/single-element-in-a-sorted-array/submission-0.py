class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if middle % 2 == 0:
                if nums[middle] != nums[middle + 1]:
                    right = middle
                else:
                    left = middle + 1
            else:
                if nums[middle] != nums[middle + 1]:
                    left = middle + 1
                else:
                    right = middle

        return nums[left]