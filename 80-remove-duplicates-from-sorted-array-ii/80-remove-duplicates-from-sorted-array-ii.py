class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashmap = {}
        start = 0 
        
        while start < len(nums):
            if nums[start] not in hashmap:
                hashmap[nums[start]] = 0
            hashmap[nums[start]] += 1
            if hashmap[nums[start]] > 2:
                hashmap[nums[start]] -= 1
                nums.pop(start)
            else:   
                start+=1
            