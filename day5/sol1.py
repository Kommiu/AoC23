from collections import defaultdict


with open(0) as f:
    lines = f.readlines()

conversions = defaultdict(dict)
seeds = [int(x) for x in lines[0].split(":")[1].strip().split(" ")]
maps = defaultdict(list)
source2dest = dict()
source = ""
for line in lines[1:]:
    if not line.strip():
        continue
    if ":" in line:
        source, _, dest = line.split(" ")[0].split("-")
        source2dest[source] = dest
        print(source, dest)
        continue
    dest_start, source_start, length = [int(x) for x in line.strip().split(" ")]
    maps[source].append((source_start, dest_start, length))


def convert(source, value):
    while source in maps:
        for ss, ds, l in maps[source]:
            if ss <= value <= ss + l:
                value = ds + (value - ss)
                break
        source = source2dest[source]
    return value


print("converting")
print(min(convert("seed", x) for x in seeds))
