# funkcja any()
# sprawdza, czy jakikolwiek element jest TRUE
# chcemy sprawdzi, czy w liscie jest jakikolwiek wlement parzysty

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers2 = [1, 3, 5, 7, 9]

def any_even(list_to_check):
    for element in list_to_check:
        if element % 2 == 0:
            return True
    return False

# if any_even(numbers2):
#     print("Znalazłem liczbę parzystą")
# else:
#     print("Nie ma liczby parzystej")

if any(numbers2):
    print("Znalazłem liczbę parzystą")
else:
    print("Nie ma liczby parzystej")

numbers3 = [element % 2 for element in numbers]
print(any(numbers3))

