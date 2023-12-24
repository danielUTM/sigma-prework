def find_max_min(list_of_ints: list) -> list:
    min_int = list_of_ints[0]
    max_int = list_of_ints[0]

    for i in list_of_ints:
        if min_int > i:
            min_int = i
        if max_int < i:
            max_int = i

    return [min_int, max_int]

user_input = list(map(int, input("Please enter list of integers (e.g. 1, 2, 3): ").split(", ")))
print(find_max_min(user_input))