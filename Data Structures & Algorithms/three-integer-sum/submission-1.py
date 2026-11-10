class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        i = 0

        while i < n - 2:
            while i < n - 2 and i > 0 and nums[i] == nums[i - 1]:
                i += 1

            if i >= n - 2:
                break

            j = i + 1
            k = n - 1
            target = -nums[i]

            while j < k:
                if nums[j] + nums[k] == target:
                    ans.append([nums[i], nums[j], nums[k]])

                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    j += 1
                    k -= 1

                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1

            i += 1

        return ans