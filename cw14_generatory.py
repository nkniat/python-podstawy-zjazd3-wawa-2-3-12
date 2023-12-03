import sys

# wyrazenie listowne
liczbyParzyste = [element
                  for element in range(10000)
                  if element % 2 == 0
                  ]

# generator
liczbyParzysteGenerator = (element
                            for element in range(10000)
                            if element % 2 == 0
                           )

wynik = 0
for element in liczbyParzysteGenerator:
    # print("Kolejna liczba parzysta to: ", element)
    wynik += element

print(wynik, "to suma liczb parzystych")

print("Liczby parzyste za pomocom wyrażenia: ", liczbyParzyste)
print("wielkość elementu liczbyParzyste: ", sys.getsizeof(liczbyParzyste))

print("Liczby parzyste za pomocom generatora: ", liczbyParzysteGenerator)
print("wielkość elementu liczbyParzysteGenerator: ", sys.getsizeof(liczbyParzysteGenerator))
# print("Liczby parzyste za pomocom generatora: ", next(liczbyParzysteGenerator))

