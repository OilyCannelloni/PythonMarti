"""
n = int(input())
ls = list(map(int, input().split()))
ct = ls[0] + ls[-1]

for i in range(1, n-1):
    if ls[i] or (ls[i-1] and ls[i+1]):
        ct += 1

print(ct)
"""


spam, ls = input(), list(map(int, input().split()))
print(sum([1 if ls[i] or (ls[i-1] and ls[i+1]) else 0 for i in range(1, len(ls)-1)]) + ls[0] + ls[-1])
