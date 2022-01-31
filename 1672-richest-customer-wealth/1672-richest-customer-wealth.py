class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        
        for account in accounts:
            max_wealth = max(sum(account), max_wealth)
        return max_wealth