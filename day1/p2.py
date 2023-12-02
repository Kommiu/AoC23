import sys
from typing import Mapping

DIGITS: Mapping[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def compare(line, start, pattern):
    end = start + len(pattern)
    return line[start:end] == pattern


def parse(line: str, start: int = 0, skip: int = 1) -> int:
    idx = start
    while not (char := line[idx]).isdigit():
        for key, val in DIGITS.items():
            if len(line) - idx > len(key) and compare(line, idx, key):
                return val
        idx += skip
    return int(char)


if __name__ == "__main__":
    result = 0
    for line in sys.stdin.readlines():
        result += 10 * parse(line)
        result += parse(line, len(line) - 1, -1)
    print(result)
