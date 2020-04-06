"""
Pomysł:
0. Eliminujemy okręgi, które zawierają (0, 0) - są one trafione zawsze
1. Obliczamy kąty skierowane półprostych stycznych do wszystkich okręgów, które przechodzą przez (0, 0)
2. Dla każdej stycznej zapamiętujemy, po której stronie swojego okręgu się znajduje
3. Sortujemy styczne rosnąco pod względem kątów
4. Iterujemy się po stycznych dodając 1 jeśli styczna jest po prawej od okręgu (wchodzimy w nowy okrąg)
   i odejmując 1, jeśli styczna jest po lewej od okręgu (wychodzimy z okręgu)
5. Bierzemy maksimum max z tego ciągu. Jest to najbardziej optymalny strzał.
6. Strzelamy k razy w ten sposób i otrzymujemy k*max trafień, co jest wynikiem
"""


from math import sqrt, atan, pi  # Pierwiastkowanie, arctangens i pi
from functools import cmp_to_key  # Definicja własnego klucza sortującego - więcej poniżej


def get_tangents(x, y, r):
    """
    Funkcja, która oblicza i zwraca kąty skierowane stycznych
    do danego okręgu.
    :param x: Współrzędna X środka okręgu
    :param y: Współrzędna Y środka okręgu
    :param r: Promień okręgu
    :return: (a, b) - kąty nachylenia kolejno prawej i lewej stycznej
    """
    alpha = pi/2 if x == 0 else atan(y/x)  # Kąt między OX a (X, Y) - unikamy dzielenia przez zero dla pionowej prostej
    beta = atan(r/sqrt(x**2+y**2-r**2))  # Kąt między styczną a prostą |(0, 0) -> (X, Y)|
    if (y > 0 and x < 0) or (y <= 0 and x <= 0):  # Dodajemy czasami pi, aby kąty były skierowane od osi X
        alpha += pi
    return (alpha - beta) % (2*pi), (alpha + beta) % (2*pi)  # Zwracamy kąty dwóch stycznych modulo 2pi


def compare_tangents(t1, t2):
    """
    Funkcja, która definiuje kolejność stycznych (kąt, zmiana) przy sortowaniu
    :param t1: Pierwsza styczna
    :param t2: Druga styczna
    """
    if t1[0] != t2[0]:  # Najpierw sortujemy po kącie rosnąco
        return t1[0] - t2[0]
    return -1 if t1[1] == 1 else 1  # Jeśli kąt jest taki sam, bierzemy najpierw "prawą" styczną -
                                    # mamy do czynienia z okręgami ze wspólną styczną, strzelając według niej
                                    # trafiamy obydwa. Dlatego najpierw wchodzimy do nowego okręgu, a potem
                                    # wychodzimy ze starego.


circles_count, bullets, goal = map(int, input().split())  # Wczytujemy kolejno n, k, m

covering = 0  # Liczba okręgów zawierających (0, 0)
starting = 0  # Liczba okręgów przecinających prostą y = 0, aby zastosować ten algorytm musimy wiedzieć,
              # ile okręgów trafiamy "na starcie"
tangents = []  # Lista, do której dopisujemy pary (kąt, wartość), gdzie wartośc to 1 dla prawej stycznej
               # i -1 dla lewej

for _ in range(circles_count):  # Dla każdego okręgu
    x, y, r = map(int, input().split())  # Wczytujemy dane
    distance_to_origin = x**2 + y**2  # Obliczamy kwadrat odległości od (0, 0)
    if distance_to_origin <= r**2:  # Jeśli jest mniejszy od r^2, okrąg pokrywa (0, 0)
        covering += 1
        continue  # Nie liczymy stycznych, gdyż takowe nie istnieją, a okrąg jest trafiany zawsze
    elif abs(y) <= r and x > 0:  # Jeśli okrąg nie pokrywa środka i spełnia te warunki, to przecina półprostą y=0, x>=0
        starting += 1

    # Jeśli okrąg nie jest patologiczny, obliczamy styczne (opisane wyżej)
    right, left = get_tangents(x, y, r)
    # Dodajemy je do listy, prawe styczne z "1", lewe z "-1"
    tangents.extend(((right, 1), (left, -1)))


# Sortujemy styczne rosnąco według kąta i strony (opisane wyżej)
tangents.sort(key=cmp_to_key(compare_tangents))

# Dla okręgów, które są styczne do półprostej o kącie 0 od góry, zmieniamy ich wartość na 0,
# gdyż już w nie na starcie "weszliśmy". Okręgów stycznych od dołu nie ruszamy, bo nadal musimy z nich "wyjść"
# Pętla while żeby oszczędzać pamięć i czas, chociaż to jest brzydkie, ale chyba najefektywniejsze w pythonie
i = 0
while tangents[i] == (0, 1):
    tangents[i] = (0, 0)
    i += 1

# Obracamy naszą półprostą w lewo i patrzymy na wejścia i wyjścia z okręgów - zapisujemy najwyższą wartość
# powstałą podczas człego obrotu
hits = starting
max_hits = starting
for tangent in tangents:
    hits += tangent[1]
    if hits > max_hits:
        max_hits = hits

# Wszystkie trafieia to najbardziej optymalny strzał * liczba pocisków
total_hits = (covering + max_hits) * bullets

# Sprawdzamy, czy wygraliśmy zakład z kolegami
if total_hits >= goal:
    print(total_hits)
else:
    print("NIE")
