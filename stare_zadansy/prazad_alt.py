s = input()
merge = int(len(s) - (len(s) - s.count('a'))/2)
print(s[:merge] if "".join([l for l in s[:merge] if l != 'a']) == s[merge:] else "NIE")
