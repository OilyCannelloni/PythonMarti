n, l, a = map(int, input().split())
time = 0
ct = 0
for _ in range(n):
    beg, dur = map(int, input().split())
    ct += (beg - time)//a
    time = beg+dur

ct += (l-time)//a

print(ct)
