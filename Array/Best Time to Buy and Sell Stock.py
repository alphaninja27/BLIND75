class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = min(prices)
        maxi = max(prices[mini:])
        if prices == prices.sort(reverse = True):
            return 0
        else:
            return maxi - mini
