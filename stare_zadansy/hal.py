n = int(input())
x = [*input().split(), '1']

ls = [x[i] for i in range(n) if x[i+1] == '1']

print(len(ls))
print(*ls)
