from os import wait
from math import prod

LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def parse(cube):
    a, b = cube.split(" ")
    return b, int(a)


def parse_draw(draw: str):
    res = dict(parse(x) for x in draw.split(", "))
    return res


def parse_line(line: str):
    game, draws = line.split(":")
    game_number = int(game[5:])


with open(0) as f:
    result = 0
    for line in f.readlines():
        temp = {"red": 0, "green": 0, "blue": 0}
        game, draws = line.split(":")
        game_number = int(game[5:])
        for draw in draws.strip().split(";"):
            for col, val in parse_draw(draw.strip()).items():
                temp[col] = max(temp[col], val)
        result += prod(temp.values())
    print(result)
