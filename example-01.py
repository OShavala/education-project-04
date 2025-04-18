def calculate_value(list):
    total = 0
    for number in list:
        total += number
    return total

# Приклад використання
list_numbers = [1, 2, 3, 4, 6]
result = calculate_value(list_numbers)
print("Sum of list:", result)

