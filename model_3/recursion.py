def get_multiplied_digits(number: int) -> int:
    str_number = str(number)
    first = int(str_number[0])

    if len(str_number) > 1 and (other := int(str_number[1:])) != 0:
        first *= get_multiplied_digits(other)

    return first


result = get_multiplied_digits(40203)
print(result)
result = get_multiplied_digits(0)
print(result)
result = get_multiplied_digits(4020300000)
print(result)
result = get_multiplied_digits(423)
print(result)
result = get_multiplied_digits(20568025)
print(result)
