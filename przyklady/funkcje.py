"""
Funkcje to takie maszynki, do których wrzucamy argumenty,
a one wypluwają wynik
"""


def dodaj_dwa(x):
    return x + 2


def suma(a, b, c):
    return a + b + c


dodaj_dwa(7)  # 9
suma(1, 2, 4)  # 7

"""
Funkcje mogą nic nie zwracać
"""


def wyprintuj_z_opisem(x):
    print("liczba jest równa " + str(x))


wyprintuj_z_opisem(7)

"""
Funkcje mogą mieć dużo kodu w środku
"""


def czy_to_samo(a, b):
    if a == b:
        return True
    else:
        return False


czy_to_samo(1, 4)  # False


"""
Przykłady:
"""


def policz_ile_w_liscie(szukany_element, lista):
    znalezione = 0
    for element in lista:
        if element == szukany_element:
            znalezione += 1

    return znalezione


lista = [1, 2, 2, 5, 2, 1, 6, 1, 1, 9]
policz_ile_w_liscie(1, lista)  # 4
policz_ile_w_liscie("a", "marysia lubi pythona")  # 3 (dlaczego?)


def suma_cyfr_liczby(liczba):
    liczba_str = str(liczba)  # zamieniamy liczbę na słowo
    cyfry = list(map(int, liczba_str))  # zamieniamy każdą "cyfro-literę" na inta
    return sum(cyfry)


print(suma_cyfr_liczby(3432))  # 12