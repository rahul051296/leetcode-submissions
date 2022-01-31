class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_freq = {}
        windowStart = 0
        max_length = 0
        for windowEnd in range(len(fruits)):
            if fruits[windowEnd] not in fruit_freq:
                fruit_freq[fruits[windowEnd]] = 0
            fruit_freq[fruits[windowEnd]] += 1
            while len(fruit_freq) > 2:
                start = fruits[windowStart]
                fruit_freq[start] -= 1
                if fruit_freq[start] == 0:
                    del fruit_freq[start]
                windowStart+=1
        
            max_length = max(max_length, windowEnd - windowStart + 1)
        return max_length