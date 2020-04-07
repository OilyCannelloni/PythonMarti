dane = input()  # RRFFFR
liczba_kwiatkow = len(dane)  # 6

kwiatki_przed = [0] * (2 * liczba_kwiatkow - 1)

i = 0
for kwiatek in dane:
    kwiatki_przed[i] = kwiatek
    i += 2

kwiatki_po = [0] * (2 * liczba_kwiatkow - 1)


for pozycja, kwiatek in enumerate(kwiatki_przed):
    if kwiatek == 0:
        continue

    for pozycja2, drugi_kwiatek in enumerate(kwiatki_przed[pozycja+1:]):
        if kwiatek == drugi_kwiatek:
            pozycja2 += pozycja + 1
            pozycja_nowa = int((pozycja + pozycja2)/2)
            kwiatki_po[pozycja_nowa] += 1


print(*kwiatki_po)
