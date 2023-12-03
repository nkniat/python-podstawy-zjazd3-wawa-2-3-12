import time
import math

def silnia_iteracja(n):
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik

def silnia_rekurencyjnie(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia_rekurencyjnie(n - 1)

"""
Na czym polega rekurencja?

silnia_rekurencyjnie(5)
5 * silnia_rekurencyjnie(4)
5 * 4 * silnia_rekurencyjnie(3)
5 * 4 * 3 * silnia_rekurencyjnie(2)
5 * 4 * 3 * 2 * silnia_rekurencyjnie(1)
5 * 4 * 3 * 2 * 1 (warunek bazowy)
"""

def silnia_modul_math(n):
    return math.factorial(n)

start = time.perf_counter()
#print("Wynik iteracyjnie", silnia_iteracja(10))
silnia_iteracja(996)
koniec = time.perf_counter()
wynik = koniec - start
print("Czas trwania silnia_iteracja() to: {:.10f}".format(wynik))


# start = time.perf_counter()
# silnia_rekurencyjnie(996)
# koniec = time.perf_counter()
# wynik = koniec - start
# print("Czas trwania silnia_rekurencyjnie() to: {:.10f}".format(wynik))


start = time.perf_counter()
silnia_modul_math(996)
koniec = time.perf_counter()
wynik = koniec - start
print("Czas trwania silnia_modul_math() to: {:.10f}".format(wynik))
