class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        
        for num in nums:
            hashmap[num] += 1
        
        for k, v in hashmap.items():
            if v == 1:
                return k