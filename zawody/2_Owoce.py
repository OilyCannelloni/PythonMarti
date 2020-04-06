liczba_skrzynek, liczba_zapytan = list(map(int, input().split()))
skrzynki = list(map(int, input().split()))

for k in range(liczba_zapytan):
    pierwsza, ostatnia = list(map(int, input().split()))
    suma = sum(skrzynki[pierwsza-1:ostatnia])
    print(suma)
