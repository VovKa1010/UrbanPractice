def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(2)
print_params(3, "bbb")
print_params(3, ["g", 2], False)
print_params(a=25)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [4, "ggg", 0]
values_dict = {"a": 5, "b": "hhh", "c": 1}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [7, "kkk"]
print_params(*values_list_2, 42)

values_list_3 = [7, "kkk"]
values_dict_3 = {"c": 1}
print_params(*values_list_2, **values_dict_3)

