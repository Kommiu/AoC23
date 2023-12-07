from collections import defaultdict

from itertools import islice

with open(0) as f:
    lines = f.readlines()

conversions = defaultdict(dict)
seeds = [int(x) for x in lines[0].split(":")[1].strip().split(" ")]
assert len(seeds) % 2 == 0
maps = defaultdict(list)
source2dest = dict()
source = ""
for line in lines[1:]:
    if not line.strip():
        continue
    if ":" in line:
        source, _, dest = line.split(" ")[0].split("-")
        source2dest[source] = dest
        continue
    dest_start, source_start, length = [int(x) for x in line.strip().split(" ")]
    maps[source].append(
        (source_start, source_start + length - 1, dest_start - source_start)
    )

for l in maps.values():
    l.sort(key=lambda x: x[0])


def convert_range(source, start, end):
    results = list()
    for left, right, shift in maps[source]:
        if end < left:
            results.append((start, end))
            return results
        if start < left:
            results.append((start, left - 1))
            start = left
        if start <= right:
            if end <= right:
                results.append((start + shift, end + shift))
                return results
            else:
                results.append((start + shift, right + shift))
                start = right + 1

    results.append((start, end))
    return results


def convert(source, ranges):
    while source in maps:
        new_ranges = set()
        for start, end in ranges:
            new_ranges.update(convert_range(source, start, end))
        ranges = sorted(new_ranges)
        source = source2dest[source]
    return ranges


def batched(iterable, n):
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


seed_ranges = sorted([(s, s + l) for s, l in batched(seeds, 2)])
print(convert("seed", seed_ranges)[0][0])
