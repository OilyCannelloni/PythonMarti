arr = list(map(int, input().split(" ")))
p, n = [sum(list(filter(fun, arr))) for fun in (lambda x: not x % 2, lambda x: x % 2)]
[print("liczba {0} wynosi {1}".format(a, b)) for a, b in [("zoledzi", p), ("kasztanow", n)]]
print("wiecej zebral Jas" if n > p else ("wiecej zebrala Ola" if n < p else "zebrali po rowno"))
print("roznica miedzy liczba kasztanow i orzechow wynosi", abs(p - n))
