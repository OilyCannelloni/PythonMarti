def cpp_is_crap():
    n, a, b = map(int, input().split())
    guyz = list(map(int, input().split()))
    m = min(a, b)
    price = 0
    half = int(len(guyz) / 2)

    if n % 2 and not guyz[half]:
        price += m

    pairs = list(zip(guyz[:half], guyz[-1:half:-1]))

    for pair in pairs:
        if pair == (0, 0):
            price += 2*m
        elif pair[0] == pair[1]:
            continue
        elif 0 in pair:
            price += b if sum(pair) == 2 else a
        else:
            print("NIE")
            return


cpp_is_crap()
