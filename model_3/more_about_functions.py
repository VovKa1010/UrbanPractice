def calculate_structure_sum(structure) -> int:
    res = 0

    for item in structure:
        if isinstance(item, dict):
            res += calculate_structure_sum(item.values())
            res += calculate_structure_sum(item.keys())

        if isinstance(item, (list, tuple, set)):
            res += calculate_structure_sum(item)

        if isinstance(item, str):
            res += len(item)

        if isinstance(item, (int, float)):
            res += item

    return res


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
