for i in range(10):
    print(str(i)*i)

print("\n\n")

for i in list(range(9))+list(range(9, 0, -1)):
    print(str(i)*i)

print("\n\n")

for i in list(range(4))+list(range(4, -1, -1)):
    print("*"*2**i)

print("\n\n")

s = input("Podaj znak")
w, h = [int(input("Podaj {}: ".format(i))) for i in ("szerokosc", "wysokosc")]
print(" ")

for i in range(h):
    print(s*w)

print("\n\n")

for i in range(h):
    if i == 0 or i == h-1:
        print(s*w)
    else:
        print(s+" "*(w-2)+s)

