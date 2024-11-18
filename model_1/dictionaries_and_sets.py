my_dict = {
    "Tom": 20,
    "Roma": 21,
    "Dima": 19
}

print(my_dict, my_dict["Tom"], my_dict.get("Fed"), sep="\n")

my_dict.update({
    "Tera": 4.543,
    "Lover": 50
})

print(my_dict.pop("Tom"), my_dict, sep="\n")


my_set = {1, 5, 2, 4, 1, 5, 1, 6, 8, "g", "r", "r", "y"}

print("\n\n", my_set, sep="")

my_set.update({7, "h"})

print(my_set)

my_set.remove(1)

print(my_set)
