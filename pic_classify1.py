from PIL import Image, ImageDraw
import random
import numpy as np
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from os import walk

# For proper work setup environment. Read more in ./pic_classify_env_README.md

k_colors = 8
k_neighbors = 3
teach = []
target_teach = []
val = []
target_val = []
mode = 'auto'  # 'auto' or 'ball_tree' or 'kd_tree' or 'brute'
n_job = 4
w = 'uniform'       # 'uniform' or 'distance'
m_colors = KMeans(k_colors, random_state=0, tol=1, max_iter=100)
# Be ready for some bad code
# HERE IT COMES

# Aivazovskiy 0
Ai_path = "./dataset/artists/Aivazovskiy/"
(_, _, Ai_filenames) = next(walk(Ai_path))
print("Aivazovskiy", Ai_filenames)
ai_val = random.randint(0, 3)
for i in range(0, 4):
    a = np.asarray(Image.open(Ai_path + Ai_filenames[i])).reshape((-1, 3))
    if i != ai_val:
        teach.append(a)
        m_colors.fit(a)
        target_teach.append(0)
    else:
        val.append(a)
        target_val.append(0)
# Brullov 1
Br_path = "./dataset/artists/Brullov/"
(_, _, Br_filenames) = next(walk(Br_path))
print("Brullov", Br_filenames)
br_val = random.randint(0, 3)
for i in range(0, 4):
    a = np.asarray(Image.open(Br_path + Br_filenames[i])).reshape((-1, 3))
    if i != br_val:
        teach.append(a)
        m_colors.fit(a)
        target_teach.append(1)

    else:
        val.append(a)
        target_val.append(1)
# da_Vinci 2
da_path = "./dataset/artists/da_Vinci/"
(_, _, da_filenames) = next(walk(da_path))
print("da_Vinci", da_filenames)
da_val = random.randint(0, 3)
for i in range(0, 4):
    a = np.asarray(Image.open(da_path + da_filenames[i])).reshape((-1, 3))
    if i != da_val:
        teach.append(a)
        m_colors.fit(a)
        target_teach.append(2)

    else:
        val.append(a)
        target_val.append(2)
# Mone 3
mn_path = "./dataset/artists/Mone/"
(_, _, mn_filenames) = next(walk(mn_path))
print("Mone", mn_filenames)
mn_val = random.randint(0, 3)
for i in range(0, 4):
    a = np.asarray(Image.open(mn_path + mn_filenames[i])).reshape((-1, 3))
    if i != mn_val:
        teach.append(a)
        m_colors.fit(a)
        target_teach.append(3)

    else:
        val.append(a)
        target_val.append(3)
# Sezann 4
Sz_path = "./dataset/artists/Sezann/"
(_, _, Sz_filenames) = next(walk(Sz_path))
print("Sezann", Sz_filenames)
Sz_val = random.randint(0, 3)
for i in range(0, 4):
    a = np.asarray(Image.open(Sz_path + Sz_filenames[i])).reshape((-1, 3))
    if i != Sz_val:
        teach.append(a)
        m_colors.fit(a)
        target_teach.append(4)

    else:
        val.append(a)
        target_val.append(4)

for arr in teach, val:
    for i in range(0, len(arr)):
        arr[i] = m_colors.predict(arr[i])
        curr_arr = []
        for j in range(0, k_colors):
            curr_arr.append(list(arr[i]).count(j))
        arr[i] = curr_arr
m_classes = KNeighborsClassifier(n_neighbors=k_neighbors, weights=w, algorithm=mode, n_jobs=n_job)
m_classes.fit(teach, target_teach)
print(target_val, m_classes.predict(val))

# for i in range(0, len(teach)):
#     teach[i] = m_colors.predict(teach[i])
#     a = []
#     for j in range(0, k_colors):
#         a.append(teach[i].count(j))
#     teach[i] = a

# for i in range(0, len(val)):
#     val[i] = m_colors.predict(val[i])
#     a = []
#     for j in range(0, k_colors):
#         a.append(val[i].count(j))
#     val[i] = a

