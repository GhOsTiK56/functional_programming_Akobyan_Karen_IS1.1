def maxProfit(prices: list[int]) -> int:

        def helper(i, min_price, max_profit):
            if i == len(prices):
                return max_profit
            # обновляем минимальную цену
            min_price = min(min_price, prices[i])
            # обновляем максимальную прибыль
            max_profit = max(max_profit, prices[i] - min_price)
            # рекурсивный вызов хвостовой рекурсии
            return helper(i + 1, min_price, max_profit)

        return helper(0, float('inf'), 0)

prices = [7,1,5,3,6,4]
print(maxProfit(prices))