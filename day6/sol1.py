from math import sqrt, floor, ceil

with open(0) as f:
    times = [int(x) for x in f.readline().split(":")[1].strip().split(" ") if x]
    distances = [int(x) for x in f.readline().split(":")[1].strip().split(" ") if x]


def solve(time, distance):
    D = sqrt(time**2 - 4 * distance)
    return floor(1 / 2 * (time - D)) + 1, ceil(1 / 2 * (time + D)) - 1


result = 1
for time, distance in zip(times, distances):
    a, b = solve(time, distance)
    print(a, b)
    result *= b - a + 1

print(result)
