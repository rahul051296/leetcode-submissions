class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums.copy()
        self.nums = nums
    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        n = len(self.nums)
        for i in range(n):
            rand = random.randrange(i, n)
            temp = self.nums[i]
            self.nums[i] = self.nums[rand]
            self.nums[rand] = temp
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()