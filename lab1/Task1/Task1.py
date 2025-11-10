from functools import lru_cache

def climbStairs(n: int) -> int:
    @lru_cache(None)  # мемоизация
    def dp(i):
        if i <= 2:
            return i
        return dp(i - 1) + dp(i - 2)

    return dp(n)

n = 5
print(climbStairs(n))
