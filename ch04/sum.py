def sum(arr):
    total = 0
    for x in arr:
        total = total + x
    return total


arr = [1, 2, 3, 4, 5]
total = sum(arr)
print(total)