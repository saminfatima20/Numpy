import numpy as np
import imageio
import matplotlib.pyplot as plt

img = imageio.imread('your_image.jpg')  

gray = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])

plt.imshow(gray, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
plt.show()
