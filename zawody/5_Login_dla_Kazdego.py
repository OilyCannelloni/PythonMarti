imie, nazwisko = input().split()

i = 1
while i < len(imie) and imie[i] < nazwisko[0]:
    i += 1

login = imie[:i] + nazwisko[0]

print(login)
