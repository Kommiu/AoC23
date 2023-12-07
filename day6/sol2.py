from math import sqrt, floor, ceil

with open(0) as f:
    time = int(f.readline().split(":")[1].strip().replace(" ", ""))
    distance = int(f.readline().split(":")[1].strip().replace(" ", ""))


def solve(time, distance):
    D = sqrt(time**2 - 4 * distance)
    return floor(1 / 2 * (time - D)) + 1, ceil(1 / 2 * (time + D)) - 1


a, b = solve(time, distance)
print(b - a + 1)
