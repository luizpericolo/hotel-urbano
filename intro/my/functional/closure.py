def make_multiplier_of(n):
    def multiplier(x):
        return n * x

    return multiplier

times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)

print(times3(5))
print(times5(3))

def acc_builder():
    acc = 0

    def accum(val):
        nonlocal acc
        acc += val
        return acc

    return accum


def get_label_builder(start='A'):
    curr_label = ord(start) - 1

    def get_next_label(step=1):
        nonlocal curr_label
        curr_label += step
        return chr(curr_label)

    return get_next_label


get_label = get_label_builder()
for i in range(26):
    print(get_label())

acc = acc_builder()
for i in range(1, 11):
    print(acc(i))
