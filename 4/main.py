# coding=utf-8


with open("input.txt") as f:
    inp = [
        [
            set(range(t[0], t[1] + 1))
            for t in (list(map(int, i.split("-"))) for i in e.split(","))
        ]
        for e in f.read().splitlines()
    ]

# PART 1
print(sum((i[0] & i[1]) in (i[0], i[1]) for i in (e for e in inp)))

# PART 2
print(sum(bool(i[0] & i[1]) for i in (e for e in inp)))
