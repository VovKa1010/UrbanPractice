first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

count_equals = 0
if first == second == third:
    count_equals = 3
elif first == second or first == third or second == third:
    count_equals = 2

print(count_equals)
