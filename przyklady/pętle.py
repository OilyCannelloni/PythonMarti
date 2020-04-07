"""
Pętle wykonują kod, który jest w nich, wiele razy
"""

"""
Pętla for - wykonuje swoją zawartość dla każdego (FOR every)
elementu listy. Składnia:
for {1} in {2}:
    robimy cos
    
{1} nazywamy jakoś zmienną, która przyjmuje kolejne wartości z listy
{2} lista, na której operujemy
"""

lista = [1, 5, 9, 2]
for element in lista:
    print(element + 2)

# Output:
# 3
# 7
# 11
# 4

"""
Trik z powtarzaniem ileś razy:
range(n) zwraca listę [0, 1, 2, ..., n-1],
więc for i in range(n) wykona kod dokładnie n razy,
i będzie przyjmowało kolejne liczby
"""

for i in range(3):
    print("hello" + str(i))

# Output:
# hello0
# hello1
# hello2

"""
Przykłady:
"""

for litera in "papaja":
    if litera == "a":
        print("a")
    else:
        print("nie a")

# Output:
# nie a
# a
# nie a
# a
# nie a
# a

lista = [1, 2, 9, 8, 4]
for pozycja in range(len(lista)):
    print(lista[:pozycja])

# Output:
# []
# [1]
# [1, 2]
# [1, 2, 9]
# [1, 2, 9, 8]

lista = []
for i in range(5):
    lista.append(2*i)

print(lista)

# Output:
# [0, 2, 4, 6, 8]





"""
Pętla while - wykonuje swoją zawartość dopóki warunek jest spełniony
"""

x = 0
while x < 4:
    print(x)
    x += 1

# Output:
# 0
# 1
# 2
# 3

string = "mmmmm, ale pyszne"
pozycja = 0
licznik = 0
while string[pozycja] == "m":
    licznik += 1
    pozycja += 1

print(licznik)  # 5 (dlaczego?)
