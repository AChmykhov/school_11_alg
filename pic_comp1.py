from PIL import Image, ImageDraw
import random
import numpy as np

INF = 1e9
mode = 'RGB'
im = Image.open('Lenna.png')
nimg = Image.new(mode, im.size)
draw = ImageDraw.Draw(nimg)
pix = im.getdata()

k = 256
claster = [0] * len(pix)
centers = [[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)] for i in range(0, k)]

# print(centers, '\n')

for i in range(0, 3):
    # new clusters
    for j in range(0, len(pix)):
        p = pix[j]
        min_dist = INF
        best_cent = [-1, -1, -1]
        for l, cent in enumerate(centers):
            dist = np.linalg.norm(np.array(cent) - np.array(p))
            if dist < min_dist:
                best_cent = l
                min_dist = dist
        claster[j] = best_cent
    # new centers
    for j in range(0, k):
        r_sum = 0
        g_sum = 0
        b_sum = 0
        cnt = 0
        for l in range(0, len(pix)):
            if claster[l] == j:
                r_sum += pix[l][0]
                g_sum += pix[l][1]
                b_sum += pix[l][2]
                cnt += 1
        if cnt != 0:
            centers[j] = [r_sum // cnt, g_sum // cnt, b_sum // cnt]
        else:
            centers[j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    # print(claster)
    # print(centers, '\n')
    curr = 0
    for x in range(0, nimg.size[0]):
        for y in range(0, nimg.size[1]):
            color = centers[claster[curr]]
            draw.point((x, y), (color[0], color[1], color[2]))
            curr += 1

    nimg.show()
