import random

def wylosuj_liczby(ile, zakres):
    szczesliwe_numery = []

    while ile > 0:
        szczesliwy_numerek = random.randint(0, zakres)

        if szczesliwy_numerek in szczesliwe_numery:
            szczesliwy_numerek = random.randint(1, zakres)
        else:
            szczesliwe_numery.append(szczesliwy_numerek)
            ile -= 1

    return szczesliwe_numery

def wylosuj_liczby_lepiej(ile, zakres):
    return random.sample(range(1, zakres + 1), ile)

print(wylosuj_liczby(6, 49))
print(wylosuj_liczby_lepiej(6, 49))

