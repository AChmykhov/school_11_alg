import numpy as np
teach_text = open("./dataset/cherchill_iron_certain_speech").readline()
if len(teach_text)%2 != 0:
    teach_text = teach_text[1:]
pairs = []
count_pairs = 0
for i in range(0, len(teach_text), 2):
    if pairs.count(teach_text[i:i+2]) == 0:
        pairs.append(teach_text[i:i+2])
        count_pairs += 1
print(count_pairs, pairs, i)           #debug print
A = np.zeros((count_pairs, count_pairs))
P = np.zeros((count_pairs, count_pairs))
# for i in range(0, len(teach_text), 2):
#     curr = pairs.index(teach_text[i:i+2])
#     if i != (len(teach_text)-2):
