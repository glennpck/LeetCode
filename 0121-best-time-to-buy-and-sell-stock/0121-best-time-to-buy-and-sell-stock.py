class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        max_p = 0
        while j < len(prices):
            current_p = prices[j] - prices[i]
            if prices[i] < prices[j]:
                max_p =max(current_p,max_p)
            else:
                i = j
            j += 1
        return max_p