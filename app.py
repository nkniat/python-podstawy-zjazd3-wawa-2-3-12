# definicja funkcji
def dodawanie(a, b):
    if a > b:
        print("Dodawanie rozpoczęte")
        return a + b
        print("Dodawania zakończone")
    else:
        print("nie będe dodwał")
        return
        print("Koniec bloku")
    print("Zakończyłem funkcje")



liczba1 = -5
liczba2 = 5

# wywołanie
wynik = dodawanie(liczba1, liczba2)

print("Wynik dodawania dwóch liczb", liczba1, liczba2, "to:", wynik)
if wynik:
    print("Wszystko poszło dobrze")
else:
    print("Coś poszło nie tak")
