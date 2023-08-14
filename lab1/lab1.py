import numpy as np
import imageio.v3 as iio
from matplotlib import pyplot as plt
im=iio.imread('./masoleh_gray.jpg')
i=np.array(im);
print(i.ndim)
irev=np.flipud(i);
plt.imshow(np.concatenate((i,irev)));
plt.show();