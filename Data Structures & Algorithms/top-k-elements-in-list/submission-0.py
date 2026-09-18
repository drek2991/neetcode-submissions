import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        minHeap = []
        for num in count:
            heapq.heappush(minHeap, (count[num], num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        ans = []
        for count, num in minHeap:
            ans.append(num)
        return ans
            