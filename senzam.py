# 1.
my_list = [5, "Hello", 3.14, True, [1, 2, 3], "World", False, 7, 9.99, "python"]

# 2.
first_value = my_list[0]
middle_value = my_list[len(my_list)//2]
last_value = my_list[-1]

print("První hodnota:", first_value)
print("Střední hodnota:", middle_value)
print("Poslední hodnota:", last_value)

# 3.
numeric_values = [x for x in my_list if isinstance(x, (int, float))]
sum_of_list = sum(numeric_values)
print("Součet prvků seznamu:", sum_of_list)

# 4. 
min_value = min(numeric_values)
max_value = max(numeric_values)
print("Nejmenší hodnota:", min_value)
print("Největší hodnota:", max_value)

# 5. 
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print("Seznam bez duplicitních hodnot:", unique_list)

# 6.
my_list[0] = "jablko"
my_list[len(my_list)//2] = 42
my_list[-1] = "banan"

print("Upravený seznam po výměně hodnot:", my_list)