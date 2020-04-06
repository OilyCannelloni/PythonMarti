
ceny = {"mleko": 3,
        "jablko": 1,
        "parowki": 2,
        "ciasto": 5,
        "szynka": 6}

x = None
suma = 0
koszyk = []


print("Witaj w moim sklepie! Oto oferta:")
print("PROD. CENA")
for produkt in ceny.keys():
    print(produkt, ceny[produkt])

print("Wpisz 'koniec', by zakonczyc zakupy, 'koszyk' by wyswietlic zawartosc koszyka")

while True:
    x = input("Co chcesz kupić? Wpisz 'koniec' aby zakonczyc zakupy: ")

    if x == "koniec":
        break
    
    if x == "koszyk":
        print(koszyk)
        continue

    if x not in ceny:
        print("Niestety nie mamy tego produktu :<")
        continue

    suma += ceny[x]
    koszyk.append(x)


print("Proszę zapłacić {} pieniedzy".format(suma))
