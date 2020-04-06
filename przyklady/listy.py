"""
Listy to takie jakby zestawy danych o różnej ilości elementów
Definiujemy je w sposób:
"""
numerki_1 = [2, 5, 4, 99]

# Pusta lista
numerki_puste = []


"""
Indeksacja:
lista[k] - k-ty element listy (liczymy od 0!)
lista[a:b] - od a-tego (włącznie) do b-tego BEZ b-tego
lista[a:] - od a-tego do końca
lista[:b] - od początku do b-tego BEZ b-tego
lista[::-1] - całość od tyłu (od początku do końca co -1, czyli się cofamy)
"""
numerki = [1, 3, 7, 8, 9, 13]
a = numerki[2]  # 7
b = numerki[2:4]  # [7, 8]  (dlaczego?)
c = numerki[3:]  # [8, 9, 13]
d = numerki[:4]  # [1, 3, 7, 8]
e = numerki[::-1]  # [13, 9, 8, 7, 3, 1]

del numerki, a, b, c, d, e  # to nie ważne


"""
Operacje na listach:
lista.append(element) - dodaje element na koniec listy
lista.index(element) - zwraca numer pozycji, na której element jest w liście
lista.sort() - sortuje elementy w liście rosnąco
sum(lista) - zwraca sumę wszystkich elementów listy
len(lista) - zwraca ilość elementów w liście (długość listy)
Sklejanie: [1, 2] + [6, 7, 9] == [1, 2, 6, 7, 9]
"""

numerki = [3, 5, 2, 4]
numerki.append(27)  # numerki == [3, 5, 2, 4, 27]
a = numerki.index(5)  # a == 1 (dlaczego?)
numerki.sort()  # numerki == [2, 3, 4, 5, 27]
b = sum(numerki)  # b == 41
c = len(numerki)  # c == 5

del numerki, a, b, c  # to nie istotne


"""
Zaawansowane operacje na listach:
map(funkcja, lista) - wykonuje funkcję na wszystkich elementach listy
WAŻNE!: Nie zwraca listy, ale <map object at 0x124syf>, co czasami trzeba 
zamienić na listę przy pomocy list()
"""
# definicja funkcji - o tym więcej w pliku "funkcje.py"
def dodaj_dwa(x):  #  f(x) = x + 2
    return x + 2


# funkcja dodaje 2 do liczby:
d = dodaj_dwa(7)  # d == 9

numerki = ["3", "5", "2", "8"]
zintowane_numerki = list(map(int, numerki))  # [3, 5, 2, 8]
zmapowane_numerki = list(map(dodaj_dwa, zintowane_numerki))  # [5, 7, 4, 10]


"""
Przykłady:
"""

# Wczytanie linijki danych w formacie "1 2 3 45 611"
# i zrobienie z niej listy [1, 2, 3, 45, 611]
# BARDZO użyteczne w zadaniach
lista = list(map(int, input().split()))

del lista

# "Rozpakowywanie" listy:
lista = [4, 7, 2]
a, b, c = lista  # a == 4, b == 7, c == 2

del lista, a, b, c

# Sortowanie "w dół"
lista = [5, 1, 4, 8, 3]
lista.sort()  # sortujemy
a = lista[::-1]  # od końca

del lista, a
