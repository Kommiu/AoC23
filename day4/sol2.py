def parse_line(line):
    count = 0
    wining = line.split(":")[1].strip()
    wining, numbers = wining.split("|")
    wining = [int(x) for x in wining.strip().split(" ") if x]
    numbers = [int(x) for x in numbers.strip().split(" ") if x]
    for num in numbers:
        if num in wining:
            count += 1
    return count


wins = list()
with open(0) as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    count = parse_line(line)
    wins.append(count)

total = 0


def count(idx):
    global total
    total += 1
    for i in range(wins[idx]):
        count(idx + i + 1)


for i in range(len(wins)):
    count(i)

print(total)
