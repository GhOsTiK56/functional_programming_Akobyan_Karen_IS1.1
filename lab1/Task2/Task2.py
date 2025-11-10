def jump(nums: list[int]) -> int:
    n = len(nums)

    def dfs(level_start, level_end, jumps):
        if level_end >= n - 1:
            return jumps  # достигли конца

        # находим максимально дальнюю позицию на следующем уровне
        farthest = max(i + nums[i] for i in range(level_start, level_end + 1))
        return dfs(level_end + 1, farthest, jumps + 1)

    # начинаем с уровня, включающего только первую позицию
    return dfs(0, 0, 0)

nums = [2, 3, 1, 1, 4]
print(jump(nums))
