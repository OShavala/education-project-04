def average_value(list):
    if len(list) == 0:
        return 0
    total = sum(list)
    return total / len(list)

# Приклад використання
list_numbers = [10, 20, 30, 40, 60]
result = average_value(list_numbers)
print("Average value of list:", result)




