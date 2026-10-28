class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pfx = []
        sfx = []
        val = 1
        for i in range(len(nums)):
            val *= nums[i]
            pfx.append(val)
        val = 1
        for i in range(len(nums)-1, -1, -1):
            val *= nums[i]
            sfx.append(val)
        sfx.reverse()
        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(sfx[i+1])
            elif i == len(nums)-1:
                ans.append(pfx[i-1])
            else:
                ans.append(pfx[i-1] * sfx[i+1])
        return ans

            
