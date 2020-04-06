from math import sqrt, atan, pi
from functools import cmp_to_key


def get_tangents(x, y, r):
    alpha = pi/2 if x == 0 else atan(y/x)
    beta = atan(r/sqrt(x**2+y**2-r**2))
    if y > 0 and x < 0:
        alpha += pi
    if y <= 0 and x <= 0:
        alpha += pi
    if y < 0 and x > 0:
        pass

    return (alpha - beta) % (2*pi), (alpha + beta) % (2*pi)


def compare_tangents(t1, t2):
    if t1[0] != t2[0]:
        return t1[0] - t2[0]
    return -1 if t1[1] == 1 else 1


circles_count, bullets, goal = map(int, input().split())

covering = 0
starting = 0
tangents = []

for _ in range(circles_count):
    x, y, r = map(int, input().split())
    distance_to_origin = x**2 + y**2
    if distance_to_origin <= r**2:
        # circle is covering origin
        covering += 1
        continue
    elif abs(y) <= r and x > 0:
        starting += 1


    right, left = get_tangents(x, y, r)
    # print(*map(lambda el: round(el*360/2/pi), (right, left)))
    tangents.extend(((right, 1), (left, -1)))


tangents.sort(key=cmp_to_key(compare_tangents))
print(*map(lambda el: (360*el[0]/2/pi, el[1]), tangents))
hits = 0
max_hits = 0

i = 0
while tangents[i] == (0, 1):
    tangents[i] = (0, 0)
    i += 1

for tangent in tangents:
    hits += tangent[1]
    if hits > max_hits:
        max_hits = hits



print(*map(lambda el: (360*el[0]/2/pi, el[1]), tangents))

total_hits = covering + starting + max_hits * bullets
print(covering, starting, max_hits)
if total_hits >= goal:
    print(total_hits)
else:
    print("NIE")


