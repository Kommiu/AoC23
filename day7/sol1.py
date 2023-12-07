from collections import Counter

order = "AKQJT98765432"
strength = {c: len(order) - i for i, c in enumerate(order)}


hands = list()
with open(0) as f:
    for line in f.readlines():
        hand, bid = line.split(" ")
        hands.append((hand, int(bid)))


def get_type(hand: str):
    cnt = Counter(hand)
    return sorted(cnt.values(), reverse=True)


s = [
    (hand, get_type(hand), tuple(strength[c] for c in hand), bid) for hand, bid in hands
]

result = sum(
    x[3] * (i + 1)
    for i, x in enumerate(
        sorted(
            s,
            key=lambda x: (
                x[1],
                x[2],
            ),
        )
    )
)
print(result)
