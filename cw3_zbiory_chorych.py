NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356, 5574}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

print("Liczba wszystkich pacjentów: ", len(NFZ))

print("\nOsoby chorujące w ostatnim roku z dzielnicy Krzyki", len(chorzy_rok.intersection(krzyki)))
print("Osoby chorujące w ostatnim roku z centrum", len(chorzy_rok.intersection(centrum)))

# czy są osoby, które mieszkają w centrum i na krzykach?
print("\nSprawdzam dane")
print("\nczy są osoby, które mieszkają w centrum i na krzykach?", len(krzyki.intersection(centrum)))
print(len(krzyki.union(centrum)), "jest różne od: ", len(krzyki) + len(centrum))

# Ten, kto chorował w ostatnim miesiącu, powinien chorować w ostatnim roku
print("\nSprawdzam dane")
print("Ten, kto chorował w ostatnim miesiącu, powinien chorować w ostatnim roku")
if len(chorzy_miesiac.difference(chorzy_rok)) > 0:
    print("Coś jest nie halo")
else:
    print("Wygląda w porządku")

# usunięcie powtórzeń ze zbioru Krzyki lub Centrum
# w zależności od decyzji użytkownika

# kobiety mają pesel parzysty np. 8768, a mężczyźni nieparzysty, np: 8769
# rzodziel zbiór NFZ na dwa podzbiory
