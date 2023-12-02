import math
from enum import IntEnum

def pole_kwadratu(a):
    return a * a

def pole_prostokata(a, b):
    return a * b

def pole_kola(r):
    return math.pi * r ** 2

def pole_trojkata(a, h):
    return 0.5 * a * h

Menu_Figury = IntEnum('Menu_Figury', 'Kwadrat Prostokąt Koło Trójkąt')

print(list(Menu_Figury))

wybor = int(input("""Wybierz figurę, której pole chcesz policzyć:
1. Kwadrat
2. Prostokąt
3. Koło
4. Trójkat
"""))

if wybor == Menu_Figury.Kwadrat:
    a = float(input("Podaj długość boku kwadratu "))
    wynik = pole_kwadratu(a)
    print("Pole kwadratu to:", wynik)
elif wybor == Menu_Figury.Prostokąt:
    a = float(input("Podaj długość boku prostokąta "))
    b = float(input("Podaj długość boku prostokąta "))
    wynik = pole_prostokata(a, b)
    print("Pole prostokąta to:", wynik)
elif wybor == Menu_Figury.Koło:
    r = float(input("Podaj długość promienia koła "))
    wynik = pole_kola(r)
    print("Pole koła to:",wynik)
elif wybor == Menu_Figury.Trójkąt:
    a = float(input("Podaj długość podstawy trójkąta "))
    h = float(input("Podaj wysokość trójkąta "))
    wynik = pole_trojkata(a, h)
    print("Pole trójkąta to:", wynik)
