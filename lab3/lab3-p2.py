import cv2
import numpy as np
from matplotlib import pyplot as plt


# simple version without specifying bins
def find_a_and_b(arr=[], vmin=0, vmax=0):
    arr[arr < vmin] = vmin
    arr[arr > vmax] = vmax

    n = np.zeros((vmax - vmin + 1,), dtype=int)

    for k in arr:
        n[k] += 1

    a = vmin
    b = vmax
    d = False

    index = 0
    last = 0

    for k in n:
        if k == 0 and d is False:
            a = index
        elif k == 0 and d is True and index < b:
            b = index
        if k < last:
            d = True
        last = k
        index += 1

    xpoints = np.zeros(256)
    for r in range(256):
        xpoints[r + 1:] += 1

    return a, b


fname = 'office.jpg'
I = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)

a, b = find_a_and_b(I.ravel(), vmin=0, vmax=255)
J = (I - a) * 255.0 / (b - a)
J[J < 0] = 0
J[J > 255] = 255
J = J.astype(np.uint8)
K = cv2.equalizeHist(I)
f, axes = plt.subplots(2, 3)
axes[0, 0].imshow(I, 'gray', vmin=0, vmax=255)
axes[0, 0].axis('off')
axes[1, 0].hist(I.ravel(), 256, [0, 256])
axes[0, 1].imshow(J, 'gray', vmin=0, vmax=255)
axes[0, 1].axis('off')
axes[1, 1].hist(J.ravel(), 256, [0, 256])
axes[0, 2].imshow(K, 'gray', vmin=0, vmax=255)
axes[0, 2].axis('off')
axes[1, 2].hist(K.ravel(), 256, [0, 256])

plt.show()
