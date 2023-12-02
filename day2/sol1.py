from os import wait


LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def parse(cube):
    a, b = cube.split(" ")
    return LIMITS[b] >= int(a)


def parse_draw(draw: str):
    return all([parse(x) for x in draw.split(", ")])


def parse_line(line: str):
    game, draws = line.split(":")
    game_number = int(game[5:])


with open(0) as f:
    result = 0
    for line in f.readlines():
        game, draws = line.split(":")
        game_number = int(game[5:])
        if all([parse_draw(draw.strip()) for draw in draws.strip().split(";")]):
            result += game_number
    print(result)
