# Sumowanie liczb dodatnik w liscie
# Funkcja, która ignoruje libczy ujemne (i zera)
# i zwarac sumę liczb tylko dodatnich

def sum_positive(numbers):
    result = 0

    for number in numbers:
        if number > 0:
            result += number

    return result

def sum_positive_2(numbers):
    return sum([number for number in numbers if number > 0])


numbers = [-5, 5, 0, -5, -5.5, 10, 15]

print(sum_positive(numbers))
print(sum_positive_2(numbers))