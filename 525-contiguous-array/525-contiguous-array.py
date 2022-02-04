class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mapping = {0: 0}
        max_length = 0
        count = 0
        for i, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count +=1
            
            if count in mapping:
                max_length = max(max_length, i - mapping[count])
            else:
                mapping[count] = i
        return max_length