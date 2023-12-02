import random

x = 0
while x < 100:
    # random >> losuje z zakresu [0,1)
    # print(random.random())

    # uniform(15, 125.5) > x ze zbioru [15, 125.5)
    # print(random.uniform(15, 125.5))

    # randrange(10) x ze zbioru liczb (0,1,2,3,4,5,6,7,8,9) > tak jak działa range > [0,10)
    # print(random.randrange(0, 50, 2))

    # randint(0, 10) >> wylosuje z puli od 0 do 10 włącznie
    print(random.randint(0, 10))

    x += 1

# choice >> zwraca losowy element z kontenera
moja_lista_piosenek = ['Piosenka 1', 'Piosenka 2', 'Piosenka 3']
print("Losuje nastepujaca piosenke dla Ciebie: ", random.choice(moja_lista_piosenek))

# choices >> zwraca losowy element, ale może nadać odpowiednie wagi (i nie tylko)
# print("Losuje nastepujaca piosenke dla Ciebie: ", random.choices(moja_lista_piosenek, [1, 2, 5], k=10))
print("Losuje nastepujaca piosenke dla Ciebie: ", random.choices(moja_lista_piosenek, [0.5, 0.15, 0.35], k=10))