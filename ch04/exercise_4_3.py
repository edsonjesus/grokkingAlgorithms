# Exercise 4.3 Find the maximum number in a list
def max_number_of(my_list):
    if not my_list:
        return 0
    if len(my_list) == 1:
        return my_list[0]
    if len(my_list) == 2:
        return my_list[0] if my_list[0] > my_list[1] else my_list[1]
    temp_max = max_number_of(my_list[1:])
    return my_list[0] if my_list[0] > temp_max else temp_max


my_list = [10, 2, 7, 45, 5]
print(max_number_of(my_list))