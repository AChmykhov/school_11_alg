import numpy as np

teach_text = open("./dataset/cherchill_iron_certain_speech.txt").readline()
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
        next_curr = pairs.index(teach_text[i:i + 2])
    else:
        next_curr = curr
    A[next_curr][curr] += 1
s = np.sum(A, axis=1)
for i in range(0, count_pairs):
    for j in range(0, count_pairs):
        P[i][j] = A[i][j] / s[i]

out = ''
state = input("Enter first two symbols, for example 'I '")
if pairs.count(state) == 0:
    print("Sorry, this pair isn't known")
else:
    depth = int(input("Enter depth"))
    for i in range(0, depth):
        out += state
        v = np.zeros(count_pairs)
        v[pairs.index(state)] = 1
        state = np.random.choice(a=pairs, p=np.matmul(P, v))
print(out)
# print(P)
