# funkcja all

def czy_spelnia_wymagania(kandydat, umiejetnosci):
    return all(umiejetnosc in kandydat['umiejetnosci'] for umiejetnosc in umiejetnosci)

kandydat = {
        'Imie': 'Tomek',
        "Nazwisko": 'Kowalski',
        'umiejetnosci': ['Python', 'ISTQB']
    }

kandydaci = [
    {
        'Imie': 'Natalia',
        "Nazwisko": 'Burda',
        'umiejetnosci': ['Agile', 'Python', 'ISTQB']
    },
    {
        'Imie': 'Kasia',
        "Nazwisko": 'Burda',
        'umiejetnosci': ['C++', 'Python', 'ISTQB']
    },
    {
        'Imie': 'Tomek',
        "Nazwisko": 'Burda',
        'umiejetnosci': ['C++', 'Agile', 'Python', 'ISTQB']
    }
]


kandydaci.append(kandydat)

print(kandydaci)

wymagane_umiejetnosci = ['Python', 'C++']

for kandydat in kandydaci:
    print(kandydat)
    if czy_spelnia_wymagania(kandydat, wymagane_umiejetnosci):
        print("Kandydat jest OK")
    else:
        print("Nie spełnia wymagań")
    print('\n')
