from PIL import Image, ImageDraw
import random
import numpy as np
from sklearn.cluster import KMeans

k = 8
INF = 1e9
mode = 'RGB'
im = Image.open('dataset/Lenna.png')
size = im.size
nimg = Image.new(mode, size)
draw = ImageDraw.Draw(nimg)
pix = np.asarray(im).reshape((-1, 3))
m = KMeans(k, random_state=0, tol=1, max_iter=100)
clusters = m.fit_predict(pix)
centers = m.cluster_centers_

results = np.array([np.around(centers[i]).astype(np.uint8) for i in clusters]).reshape((*size, 3))

# print(
#     np.array(pix).shape,
#     np.array(clusters).shape,
#     np.array(centers).shape,
#     results.shape,
#     size,
#     results.dtype)
# print(results[0][:10])


nimg = Image.fromarray(results)

# curr = 0
# for x in range(0, nimg.size[0]):
#     for y in range(0, nimg.size[1]):
#         color = centers[clusters[curr]]
#         draw.point((x, y), (color[0], color[1], color[2]))
#         curr += 1

nimg.show()

# print(np.array(pix).shape,
#       np.array(clusters).shape,
#       np.array(centers).shape,
#       np.array(results).shape,
#       size,
#       results.dtype)
#
# print(clusters[:10])
