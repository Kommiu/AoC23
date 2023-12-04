with open(0) as f:
    lines = f.readlines()
result = 0
for line in lines:
    count = 0
    wining = line.split(":")[1].strip()
    wining, numbers = wining.split("|")
    wining = [int(x) for x in wining.strip().split(" ") if x]
    numbers = [int(x) for x in numbers.strip().split(" ") if x]
    for num in numbers:
        if num in wining:
            count += 1
    if count:
        result += 2 ** (count - 1)

print(result)
