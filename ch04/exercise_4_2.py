# Exercise 4.2 Write a recursive function to count the number of items in a list
def count_items(my_numbers):
    if not my_numbers:
        return 0
    return 1 + count_items(my_numbers[1:])


list_of_items = [1, 2, 3, 4, 5]
print(count_items(list_of_items))
