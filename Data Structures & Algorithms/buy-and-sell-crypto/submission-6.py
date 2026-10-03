class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0

        i = 0
        for j in range(1, n):
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                maxProfit = max(maxProfit, profit)
            elif prices[j] < prices[i]:
                i = j
        return maxProfit





        # for i in range(n):
        #     profit = 0
        #     for j in range(i+1, n):
        #         profit = prices[j] - prices[i]
        #         maxProfit = max(maxProfit, profit)
        # return maxProfit

        