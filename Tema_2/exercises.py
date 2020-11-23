# list initialise
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# print the list in ascending order
print(sorted(my_list))
print(my_list)

# print the list in descending order
print(sorted(my_list, reverse=True))
print(my_list)

# print the value from even indexes of the list
print(my_list[0::2])

# print the value from odd indexes of the list
print(my_list[1::2])

# print the values from the list that are multiples of 3
for value in my_list:
    if value % 3 == 0:
        print(value, " ", end="")
