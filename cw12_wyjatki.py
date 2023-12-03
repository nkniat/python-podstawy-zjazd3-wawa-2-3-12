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

licznik = 0
while True:
    try:
        x = int(input("Wprowadź liczbę całkowitą "))
        break
    except ValueError:
        # raise ValueError('Coś poszło nie tak')

        # try:
        #     x = float(x)
        #     print("Nie udało się zapisać jako int, jest jako float")
        # except ValueError:
        #     print("nie udało się zapisać inta jako float")
        print("Usik, to nie jest liczba całkowita")
        licznik += 1
        if licznik == 3:
            print("Wykorzystałeś 3 próby.")
            break

print("Dalsza część kodu")