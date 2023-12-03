# wykorzystanie *args - nieznana liczba argumentów
# argumenty przekazywane do krotki
def dodawanie_liczb(*liczby):
    wynik = 0
    for liczba in liczby:
        wynik += liczba
    return wynik


# **args - nieznana liczba argumentów
# argumenty przekazywane wformie klucz-wartość (słownik)
def zrobZdanie(**slowa):
    zdanie = ''
    for slowo in slowa.values():
        zdanie += slowo
        zdanie += ' '
    return zdanie
# zadanie domwe: zmodyfikuj funkcje o 'bajery', np. Pierwsze słowo musi być z wielkiej litery, zdanie ma sie kończyć kropką
# albo spytaj użytkownika, jak ma się kończyć zdanie?

print("Dodawanie wielu liczb\n wynik to: ", dodawanie_liczb(1, 2))
print("Dodawanie wielu liczb\n wynik to: ", dodawanie_liczb(1, 2, 3))
print("Dodawanie wielu liczb\n wynik to: ", dodawanie_liczb(1, 2, 3, 4))
print("Dodawanie wielu liczb\n wynik to: ", dodawanie_liczb(1, 2, 3, 4, 5.5))

print("Nowe zdanie to: ", zrobZdanie(slowo1='Python', slowo2='jest', slowo3='fajny'))

