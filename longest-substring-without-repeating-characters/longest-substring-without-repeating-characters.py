class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowStart = 0
        windowMap = {}
        max_count = 0
        for windowEnd in range(len(s)):
          
            if s[windowEnd] in windowMap:
                if windowMap[s[windowEnd]] < windowStart:
                    max_count = max(max_count, windowEnd - windowStart+1)
                else:
                    windowStart = windowMap[s[windowEnd]]+1
            else:
                max_count = max(max_count, windowEnd - windowStart+1)

            windowMap[s[windowEnd]] = windowEnd
            
    
        return max_count
            