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
