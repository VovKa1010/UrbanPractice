my_dict = {
    "Tom": 20,
    "Roma": 21,
    "Dima": 19
}

print(my_dict)
print(my_dict["Tom"])
print(my_dict.get("Fed"))

my_dict.update({
    "Tera": 4.543,
    "Lover": 50
})

print(my_dict.pop("Tom"))
print(my_dict)

my_set = {1, 5, 2, 4, 1, 5, 1, 6, 8, "g", "r", "r", "y"}

print("\n")
print(my_set)

my_set.update({7, "h"})

print(my_set)

my_set.remove(1)

print(my_set)
