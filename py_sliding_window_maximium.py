
def sliding_window_maximium(nums: list[int], k: int) -> list[int]:
    result = []
    if len(nums) < 1 or k < 1:
        return result
    for i in range(len(nums) - k + 1):
        result.append(max(nums[i:i + k]))

    return result


tests = [
    # Ejemplos del enunciado
    ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
    ([4, 2, 12, 11, -5], 2, [4, 12, 12, 11]),
    ([], 3, []),

    # Casos base
    ([1], 1, [1]),
    ([5, 4], 1, [5, 4]),
    ([5, 4], 2, [5]),

    # Todos iguales
    ([2, 2, 2, 2], 2, [2, 2, 2]),
    ([7, 7, 7, 7, 7], 3, [7, 7, 7]),

    # Creciente
    ([1, 2, 3, 4, 5], 2, [2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], 3, [3, 4, 5]),

    # Decreciente
    ([5, 4, 3, 2, 1], 2, [5, 4, 3, 2]),
    ([5, 4, 3, 2, 1], 3, [5, 4, 3]),

    # Negativos
    ([-1, -3, -2, -5, -4], 2, [-1, -2, -2, -4]),
    ([-5, -4, -3], 3, [-3]),

    # Máximo entra y sale de la ventana
    ([9, 1, 2, 3, 4], 2, [9, 2, 3, 4]),
    ([1, 9, 2, 3, 4], 3, [9, 9, 4]),
    ([4, 3, 2, 1, 5], 2, [4, 3, 2, 5]),

    # Duplicados
    ([1, 3, 3, 2, 3], 3, [3, 3, 3]),
    ([5, 5, 1, 5], 2, [5, 5, 5]),

    # k = len(nums)
    ([3, 1, 5, 2], 4, [5]),

    # k inválido
    ([1, 2, 3], 0, []),
]

for nums, k, esperado in tests:
    obtenido = sliding_window_maximium(nums, k)
    print(
        f"{'OK ' if obtenido == esperado else 'ERR'} "
        f"k={k:<2} esperado={esperado} obtenido={obtenido}"
    )