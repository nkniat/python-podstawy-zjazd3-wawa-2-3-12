# 0 1 1 2 3 5 8 13 21 34 ...

def Fibbonaci(num):
    x, y = 0, 1
    for _ in range(num):
        yield x
        x, y = y, x + y


for i in Fibbonaci(100):
    print(i)
