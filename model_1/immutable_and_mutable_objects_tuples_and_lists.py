immutable_var = (0, "2", True, [2, 3, 4])

print("Immutable tuple:")
print(immutable_var)

# кортеж неизменяемый объект при попытке изменить элемент выдает ошибку
# immutable_var[0] = 2

# но можно изменить список в кортеже
immutable_var[3][0] = 1

print(immutable_var)

mutable_list = [0, "2", True, [2, 3, 4]]

print("\nMutable list:")
print(mutable_list)

mutable_list[0] = 2
mutable_list[3][0] = 1

print(mutable_list)
