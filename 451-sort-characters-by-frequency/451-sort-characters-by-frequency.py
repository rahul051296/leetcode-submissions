class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        for c in s:
            if c not in hashmap:
                hashmap[c] = 0
            hashmap[c] += 1
        res = ''
        sorted_map = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        for k, v in sorted_map:
            res += k*v
        return res