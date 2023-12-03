# program, który na bazie wprowadzonej wypłati
# oraz liczby dzieci
# wylicza dochód na osobę

def czy_moze_byc_float(wyplata):
    try:
        wyplata = float(wyplata)
        return True
    except ValueError:
        return False

while True:
    wyplata = input("Podaj Twój dochód ")

    if czy_moze_byc_float(wyplata):
        wyplata = float(wyplata)
        print("Dane prawne, działam dalej")
        break
    else:
        print("Dane niepoprawne")
