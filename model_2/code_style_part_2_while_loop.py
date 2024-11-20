my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

i = 0
while i < len(my_list):
    item = my_list[i]
    if item > 0:
        print(item)
        i += 1
    elif item == 0:
        i += 1
    else:
        break
