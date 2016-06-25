from collections import Sequence

def s_enumerate(items, start):
    for item in items:
        yield start, item
        start += 1

def my_enumerate(items, start=0):
    iterator = iter(items)
    while True:
        yield start, next(iterator)
        start += 1

def other_enumerate(items, start=0):
    yield from zip(to_infinity(start), items)

def to_infinity(start=0):
    while True:
        yield start
        start += 1

ufs = ["RJ", "SC", "RS", "PR"]
names = ["Rio de Janeiro", "Santa Catarina", "Rio Grande do Sul", "Paraná"]

for i, uf in my_enumerate(ufs):
    print(uf, names[i])

print()

for uf, name in zip(ufs, names):
    print(uf, name)


for i, elem in other_enumerate(range(10), start=1):
    print(i, elem)
