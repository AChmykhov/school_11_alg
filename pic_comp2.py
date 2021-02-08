from PIL import Image, ImageDraw
import random
import numpy as np
from sklearn.cluster import KMeans



INF = 1e9
mode = 'RGB'
im = Image.open('Lenna.png')
nimg = Image.new(mode, im.size)
draw = ImageDraw.Draw(nimg)
pix = im.getdata()
m = KMeans(256, random_state=0, tol=1, max_iter=100)
clusters = m.fit_predict(pix)
centers = m.cluster_centers_

results = [np.around(centers[i]) for i in clusters]
nimg = Image.fromarray(results)

# curr = 0
# for x in range(0, nimg.size[0]):
#     for y in range(0, nimg.size[1]):
#         color = centers[claster[curr]]
#         draw.point((x, y), (color[0], color[1], color[2]))
#         curr += 1

nimg.show()
