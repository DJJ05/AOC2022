# coding=utf-8

with open("input.txt") as f:
    inp = f.read()
    e = sorted([sum(map(int, i)) for i in [i.split("\n") for i in inp.split("\n\n")]])

print(e[-1])
print(sum(e[-3:]))
