def sum(list):
    if not list:
        return 0
    return list[0] + sum(list[1:])


arr = [1, 2, 3, 4, 5]
total = sum(arr)
print(total)