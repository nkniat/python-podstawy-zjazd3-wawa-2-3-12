# funkcja anonimowa, funkcja bez nazwy
# szybka, ma coś wykonać i tyle

# podwoj = lambda x: x * 2
# print(podwoj(4))

def podwoj(x):
    return x * 2

print((lambda x: x * 2)(4))
print(podwoj(8))
print(podwoj((lambda x: x * 2)(8)))

numbers = [1, -2, -3, -4, 5, 6, 7, 8, 9, 10]

numbers_filtered = list(filter(lambda x: x > 0, numbers))
print(numbers_filtered)
