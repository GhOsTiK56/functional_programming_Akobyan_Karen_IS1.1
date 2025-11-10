def getRow(rowIndex: int) -> list[int]:
    # рекурсивная функция возвращает строку треугольника Паскаля
    def build_row(n):
        if n == 0:
            return [1]
        prev_row = build_row(n - 1)  # рекурсивно получаем предыдущую строку
        row = [1]
        # вычисляем элементы текущей строки через предыдущую
        for i in range(1, len(prev_row)):
            row.append(prev_row[i - 1] + prev_row[i])
        row.append(1)
        return row

    return build_row(rowIndex)

rowIndex = 3
print(getRow(rowIndex))
