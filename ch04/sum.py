def sum(arr):
    if(len(arr) == 0):
        return 0
    else:
        return arr.pop(0) + sum(arr)


arr = [1, 2, 3, 4, 5]
total = sum([])
print(total)