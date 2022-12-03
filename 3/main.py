# coding=utf-8

with open("input.txt") as f:
    inp = f.read().splitlines()

p = lambda c: ord(c) - 96 if c.islower() else ord(c) - 38

# PART 1
i = sum(
    map(
        p,
        [
            (lambda x, y: "".join({c for c in x if c in y}))(*e)
            for e in [(e[: len(e) // 2], e[len(e) // 2 :]) for e in inp]
        ],
    )
)
print(i)

# PART 2
i = sum(
    map(
        p,
        [
            (lambda x: [c for c in x[0] if c in x[1] and c in x[2]][0])(inp[i : i + 3])
            for i in range(0, len(inp), 3)
        ],
    )
)

print(i)
