worek = [int(i) for i in input().split(" ")]

suma_nieparz = 0
suma_parz = 0

for orzech in worek:
    if orzech % 2 == 0:
        suma_parz += orzech
    else:
        suma_nieparz += orzech

print("liczba kasztanow wynosi", suma_nieparz)
print("liczba zoledzi wynosi", suma_parz)


if suma_parz > suma_nieparz:
    print("wiecej owocow (zoledzi) zebrala Ola")
elif suma_parz < suma_nieparz:
    print("wiecej owocow (kasztanow) zebral Jas")
else:
    print("Ola i Jas zebrali po rowno owocow")

roznica = abs(suma_parz - suma_nieparz)
print("roznica miedzy liczba kasztanow i zoledzi wynosi", roznica)