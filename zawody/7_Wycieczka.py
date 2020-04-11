n, m = map(int, input().split())
stacje = {input(): i for i in range(n)}


odcinki = [0] * n

for _ in range(m):
    wycieczka = input().split()
    miejsca = int(wycieczka[2]) + 2*int(wycieczka[3]) + 3*int(wycieczka[4])

    for i in range(stacje[wycieczka[0]], stacje[wycieczka[1]]):
        odcinki[i] += miejsca

print(max(odcinki))


