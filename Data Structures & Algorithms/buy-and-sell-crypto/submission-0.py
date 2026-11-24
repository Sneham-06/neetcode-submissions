class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cur = 0
        best = 0

        for i in range(1, len(prices)):
            cur += prices[i] - prices[i-1]
            cur = max(cur, 0)
            best = max(best, cur)

        return best