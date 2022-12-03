# coding=utf-8

func = lambda puzinp: sum(
    [
        e[1]
        + (
            lambda x, y: 0
            if (x, y) == (1, 3) or x > y and (x, y) != (3, 1)
            else 3
            if x == y
            else 6
        )(*e)
        for e in [
            list(
                map(
                    lambda x: 1 if x in ("A", "X") else 2 if x in ("B", "Y") else 3,
                    e,
                )
            )
            for e in puzinp
        ]
    ]
)

with open("input.txt") as f:
    inp = [e.split() for e in f.read().splitlines()]

# PART 1 #
print(func(inp))

# PART 2 #
inp = [
    [
        e[0],
        e[0]
        if e[1] == "Y"
        else (lambda x: "X" if x == "C" else "Y" if x == "A" else "Z")(e[0])
        if e[1] == "Z"
        else (lambda x: "X" if x == "B" else "Y" if x == "C" else "Z")(e[0]),
    ]
    for e in inp
]
print(func(inp))
