"""
PLAN:
1. Wczytanie danych
2. Sortowanie wartości monet
3. Dajemy jeden największy i sprawdzamy co dostaniemy
4. Dajemy 2 najw. ...
5. Dajemy 3 najw ...
...
N. Dajemy wszystkko ...
N + 1: print(startowe + zysk)
"""

"""
Nasze: 12 11 5 1

Jego: 6 7 7 8 11

dajemy 1 -> dostajemy 1, zysk 0
dajemy 2 -> dostajemy 3 zysk 1

zysk = max(0, 1, 1, 0)

print(startowe + zysk)
"""


liczba_naszych, liczba_jego = list(map(int, input().split()))

nasze = list(map(int, input().split()))
jego = list(map(int, input().split()))

nasze.sort()
jego.sort()

nasze = nasze[::-1]

zyski = []

nasza_suma = 0
for k in range(liczba_naszych):
    nasza_suma += nasze[k]

    jego_suma = 0
    i = 0
    while jego_suma < nasza_suma:
        jego_suma += jego[i]
        i += 1
    i -= 1

    zysk = i - k - 1
    zyski.append(zysk)

print(liczba_naszych + max(zyski))