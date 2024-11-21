# call counter
calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string: str):
    count_calls()

    len_string = len(string)
    up_string = string.upper()
    lo_string = string.lower()
    return len_string, up_string, lo_string


def is_contains(string: str, list_to_search: list[str]):
    count_calls()

    res = False
    for item_list in list_to_search:
        if item_list.lower() == string.lower():
            res = True

    return res


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
