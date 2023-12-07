from collections import Counter

order = "AKQT98765432J"
strength = {c: len(order) - i for i, c in enumerate(order)}


hands = list()
with open(0) as f:
    for line in f.readlines():
        hand, bid = line.split(" ")
        hands.append((hand, int(bid)))


def get_type(hand):
    jokers = len([x for x in hand if x == "J"])
    hand = [x for x in hand if x != "J"]
    cnt = Counter(hand)
    values = sorted(cnt.values(), reverse=True)
    if jokers == 5:
        values = [5]
    else:
        values[0] += jokers
    return values


s = [
    (hand, get_type(hand), tuple(strength[c] for c in hand), bid) for hand, bid in hands
]

sorted_s = sorted(
    s,
    key=lambda x: (
        x[1],
        x[2],
    ),
)
# print(sorted_s)
result = sum(x[3] * (i + 1) for i, x in enumerate(sorted_s))
print(result)
