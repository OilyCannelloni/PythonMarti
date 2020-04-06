s = input()
sklej = int(len(s) - (len(s) - s.count('a'))/2)
bez_a = ""
for litera in s[:sklej]:
  if litera != 'a':
    bez_a += litera

if bez_a == s[sklej:]:
  print(s[:sklej])
else:
  print("NIE")
