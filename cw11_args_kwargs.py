def organizuj_impreze(**przyniesione_rzeczy):
    for imie, rzeczy in przyniesione_rzeczy.items():
        print(imie, "przyniósł: ", rzeczy)
# przeiteruj po liście rzeczy i wypisz je w formie numerowanej listy

# kolejnosc argumentow w funkcji
# 1. standardowe argumenty >> dane
# 2. *args
# 3. **kwargs

def dodwania_liczb(*args, tryb)  # >> źle
    pass

def dodwania_liczb(tryb, *args, **kwargs)  # >> OK
    pass


# przykład, szkielet, jak można wykorzystać kwargsy
def generuj_raport(dane, **opcje):
    if 'format' in opcje:
        if opcje['format'] == 'Excel':
            # generowanie raportu w Excelu
            print('generowanie raportu w Excelu')
        if opcje['format'] == 'PDF':
            # generowanie raportu w PDF
            print('generowanie raportu w PDF')
    else:
        print('Nie wybrano formatu raportu')
        return
    return True


organizuj_impreze(Kasia=['paluszki', 'chipsy', 'popcorn'], Jasiek=['sok pomarańczowy', 'piwo bezalkoholowe'], Krzysiek='sałatka')

dane_z_bazy = "" # jakieś dostepne dane do raportu

generuj_raport(dane_z_bazy, klient1='Excel', klient2='PDF')
generuj_raport(dane_z_bazy, klient1='Excel', klient2='CSV', klient3='txt')
