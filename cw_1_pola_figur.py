import math

def pole_kwadratu(a):
    return a * a

def pole_prostokata(a, b):
    return a * b

def pole_kola(r):
    return math.pi * r ** 2

def pole_trojkata(a, h):
    return 0.5 * a * h


wybor = input("""Wybierz figurę, której pole chcesz policzyć:
1. Kwadrat
2. Prostokąt
3. Koło
4. Trójkat
""")

if wybor == "1":
    a = float(input("Podaj długość boku kwadratu "))
    wynik = pole_kwadratu(a)
    print("Pole kwadratu to:", wynik)
elif wybor == "2":
    a = float(input("Podaj długość boku prostokąta "))
    b = float(input("Podaj długość boku prostokąta "))
    wynik = pole_prostokata(a, b)
    print("Pole prostokąta to:", wynik)
elif wybor == "3":
    r = float(input("Podaj długość promienia koła "))
    wynik = pole_kola(r)
    print("Pole koła to:",wynik)
elif wybor == "4":
    a = float(input("Podaj długość podstawy trójkąta "))
    h = float(input("Podaj wysokość trójkąta "))
    wynik = pole_trojkata(a, h)
    print("Pole trójkąta to:", wynik)
