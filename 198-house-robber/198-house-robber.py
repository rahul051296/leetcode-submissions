class Solution:

    def rob(self, nums: List[int]) -> int:
        table = [None for _ in range(len(nums) + 1)]
        
        n = len(nums)
        
        table[n] = 0
        table[n-1]= nums[n-1]
        ans = 0
        for i in range(n-2,-1,-1):
            table[i] = max(table[i+1], table[i+2] + nums[i])
        return table[0]