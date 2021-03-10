import numpy as np


def train(path):
    teach_text = open(path).readline()
    if len(teach_text) % 2 != 0:
        teach_text = teach_text[1:]
    pairs = []
    count_pairs = 0
    for i in range(0, len(teach_text), 2):
        if pairs.count(teach_text[i:i + 2]) == 0:
            pairs.append(teach_text[i:i + 2])
            count_pairs += 1
    # print(count_pairs, pairs, i, count_pairs == len(pairs))  # debug print
    A = np.zeros((count_pairs, count_pairs))
    P = np.zeros((count_pairs, count_pairs))
    for i in range(0, len(teach_text), 2):
        curr = pairs.index(teach_text[i:i + 2])
        if i != (len(teach_text) - 2):
            next_curr = pairs.index(teach_text[i + 2:i + 4])
        else:
            next_curr = curr
        A[next_curr][curr] += 1
    s = np.sum(A, axis=1)
    for i in range(0, count_pairs):
        for j in range(0, count_pairs):
            P[i][j] = A[i][j] / s[i]
    return P, A, s, pairs, count_pairs


def generate(P, pairs, count_pairs):
    out = ''
    state = input("Enter first two symbols, for example 'I '\n")
    if pairs.count(state) == 0:
        print("Sorry, this pair isn't known")
    else:
        depth = int(input("Enter depth\n"))
        for i in range(0, depth):
            out += state
            v = np.zeros(count_pairs)
            v[pairs.index(state)] = 1
            print(np.dot(P, v). shape, v.shape)
            state = np.random.choice(a=pairs, p=np.dot(P, v))
    print(out)
    print(P)


path = "./dataset/cherchill_iron_certain_speech.txt"
P, A, s, pairs, count_pairs = train(path)
# print(A, "1\n", P, "2\n", s)
# print(A.shape, s.shape, P.shape)
generate(P, pairs, count_pairs)
