from functools import lru_cache
def maxProfit(prices: list[int]) -> int:

        n = len(prices)

        @lru_cache(None)
        def dp(i, holding):
            if i == n:
                return 0
            if holding:
                return max(prices[i] + dp(i + 1, False), dp(i + 1, True))
            else:
                return max(-prices[i] + dp(i + 1, True), dp(i + 1, False))

        return dp(0, False)

prices = [7,1,5,3,6,4]
print(maxProfit(prices))