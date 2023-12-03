class Dog:
    def __init__(self, name, age):
        print("Konstuktor")
        self.name = name
        self.age = age

    def print_info(self):
        print("To jest piesek o imieniu", self.name, "a wiek to: ", self.age)



piesek1 = Dog('Faza', 13)
print(piesek1.name)  # >> Faza
print("wiek Pieska 1 to: ", piesek1.age)

piesek1.print_info()

#faza.wiek = 13
#
# pluto = Dog()
# pluto.wiek = 10
#
# burek = Dog()
# burek.wiek = 15

# wiek = 15.5
# print(wiek.is_integer())




