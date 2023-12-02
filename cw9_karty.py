import random

talia = ["9", "9", "9", "9",
        "10", "10", "10", "10",
        "J", "J", "J", "J",
        "D", "D", "D", "D",
        "K", "K", "K", "K",
        "A", "A", "A", "A",
         "Jocker"
        ]

random.shuffle(talia)
print(talia)

print("Liczba kart przed rozdaniem: ", len(talia))
print("5 kart dla gracza 1: ", random.sample(talia, 5))
print("Liczba kart po rozdaniu: ", len(talia))
print("5 kart dla gracza 2: ", random.sample(talia, 5))

gracz1 = []
gracz2 = []

for i in range(5):
    gracz1.append(talia.pop())
    gracz2.append(talia.pop())

print(gracz1)
print(gracz2)
print(len(talia))

# zadanie domowe: rozdaj karty dopóki ich nie zabraknie