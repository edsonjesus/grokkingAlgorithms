# Exercise 4.4: Recursive case for binary search
def binary_search(ordered_list, item):
    if len(ordered_list) == 0:
        return None

    low = 0
    high = len(ordered_list) - 1
    mid = round((low + high) / 2)
    guess = ordered_list[mid]

    if len(ordered_list) == 1:
        return 0 if ordered_list[0] == item else None

    if guess == item:
        return mid
    elif guess > item:
        return binary_search(ordered_list[:mid], item)
    else:
        found = binary_search(ordered_list[(mid + 1):], item)
        return (mid+1) + found if found is not None else None


my_list = [1, 2, 3, 5, 9, 10]
print(binary_search(my_list, 3))

# print(binary_search([], 3))

# print(binary_search([3], 3))

# print(binary_search([1], 3))

# my_list = [1, 3, 5, 6, 7]
# print(binary_search(my_list, 3))

# my_list = [1, 3, 5]
# print(binary_search(my_list, 3))

# my_list = [1, 3]
# print(binary_search(my_list, 3))

# my_list = [1, 2, 3, 5, 9, 10]
# print(binary_search(my_list, 25))
