def dzielenie(a, b):
    return a/b


try:
    wynik = dzielenie(10, 0)
except ZeroDivisionError:
    print("Nie dziel przez zero Ty cholero!")
else:
    print("Wynik dzielenia to:", wynik)
finally:
    print("Koniec operacji")


try:
    x = int(input("Wprowadź liczbę całkowitą "))
except ValueError:
    print("Usik, to nie jest liczb całkowita")
