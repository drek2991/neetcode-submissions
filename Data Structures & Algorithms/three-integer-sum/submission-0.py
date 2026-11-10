class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        i = 0
        while i < n-2:
            j = i+1
            k = n-1
            while j < k:
                target = -nums[i]
                if nums[j] + nums[k] == target: #found a valid triplet
                    trip = []
                    trip.append(nums[i])
                    trip.append(nums[j])
                    trip.append(nums[k])
                    ans.append(trip)
                    while j+1 < n and nums[j] != nums[j+1]:
                        j += 1
                    while k-1 > i and nums[k] != nums[k-1]:
                        k -= 1
                elif nums[j] + nums[k] < target: #sum is less, must be larger
                    j += 1
                elif nums[j] + nums[k] > target: #sum is greater, must be less than
                    k -= 1
            i += 1
        return ans



