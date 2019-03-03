data = [
    [set([1,2,3,4]), set([5,6,7,8,9,10])],
    [set([1,8,9,10]), set([2,3,7]), set([4,5,6])],
    [set([1,3,5,7,9]), set([2,4,6,8,10])]
]

index = [0] * len(data)
index_max = [len(d) for d in data]
steps = sum(index_max)

def get(data, index):
    out = data[0][index[0]]
    for i in range(1, len(index)):
        out = out & data[i][index[i]]
    return out


def add(index, index_max):
    for i in range(1, len(index) + 1):
        index[-i] += 1
        if index[-i] < index_max[-i]:
            break
        index[-i] %= index_max[-i]

out = []
for i in range(0, steps):
    out.append(get(data, index))
    add(index, index_max)

print(out)
