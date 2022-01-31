class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        queue = []
        
        for num in nums:
            heapq.heappush(queue, -num)
        
        max1, max2 = -heapq.heappop(queue), -heapq.heappop(queue)
        
        return (max1-1)*(max2-1)