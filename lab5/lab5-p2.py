import numpy as np
import cv2
from matplotlib import pyplot as plt

I = cv2.imread("agha-bozorg.jpg", cv2.IMREAD_GRAYSCALE)
Dx = np.array([[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]])
Ix = cv2.filter2D(I, cv2.CV_16S, Dx)
f, axes = plt.subplots(2, 2)
axes[0, 0].imshow(I)
axes[0, 0].set_title("Original Image")
axes[0, 0].axis('off')
axes[0, 1].axis('off')
axes[0, 1].imshow(Ix)
axes[0, 1].set_title("Sobol")
u, p = Ix.shape
for i in range(u):
    for j in range(p):
        if Ix[i][j] > 0:
            Ix[i][j] += 255
        if Ix[i][j] < 255:
            Ix[i][j] -= 255
axes[1, 0].imshow(Ix)
axes[1, 0].axis('off')
axes[1, 1].axis('off')
plt.show()
