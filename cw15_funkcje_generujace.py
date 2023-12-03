
# generator
liczbyParzysteGenerator = (element
                            for element in range(400)
                            if element % 2 == 0
                           )

# funkcja generujaca
def generuj_liczby_parzyste():
    print("start")
    for element in range(400):
        print("Przed yield")
        if element % 2 == 0:
            yield element # ...
            print("po yield")

def generuj_10_liczb():
    x = 0
    while x < 10:
        yield x
        x += 1


a = generuj_liczby_parzyste()
print(a)

print("pierwsze generowanie:", list(generuj_10_liczb()))
print("drugie generowanie:", list(generuj_10_liczb()))

tmp_10_liczb = (x
                for x in range(10))
print("pierwsze generowanie:", list(tmp_10_liczb))
print("drugie generowanie:", list(tmp_10_liczb))

