import cv2
import numpy as np
from matplotlib import pyplot as plt

f, p = plt.subplots(2, 2)

I = cv2.imread('isfahan.jpg')
p[0, 0].imshow(I)
p[0, 0].title.set_text('original')
p[0, 0].axis('off')

i = cv2.copyMakeBorder(I, 10, 10, 10, 10, cv2.BORDER_REFLECT, None, value=0)
p[1, 0].imshow(i)
p[1, 0].title.set_text('reflect')
p[1, 0].axis('off')

i = cv2.copyMakeBorder(I, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value=np.random.randint(0, 255, 3).tolist())
p[0, 1].imshow(i)
p[0, 1].title.set_text('constant')
p[0, 1].axis('off')

i = cv2.copyMakeBorder(I, 10, 10, 10, 10, cv2.BORDER_REPLICATE, None, value=0)
p[1, 1].imshow(i)
p[1, 1].title.set_text('replicate')
p[1, 1].axis('off')

plt.show()
