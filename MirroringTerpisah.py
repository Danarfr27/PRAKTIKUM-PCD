import numpy as np
import imageio as img
import matplotlib.pyplot as plt

path = 'D:\\source.jpg'[cite: 2]
image = img.imread(path)[cite: 2]
height, width = image.shape[:2][cite: 2]

horizontal = np.zeros_like(image)[cite: 2]
vertical = np.zeros_like(image)[cite: 2]

for y in range(height):[cite: 2]
    for x in range(width):[cite: 2]
        horizontal[y, x] = image[y, width - 1 - x][cite: 2]

for y in range(height):[cite: 2]
    for x in range(width):[cite: 2]
        vertical[y, x] = image[height - 1 - y, x][cite: 2]

plt.figure(figsize=(10, 5))[cite: 2]
plt.subplot(1, 3, 1)[cite: 2]
plt.title("Original")
plt.imshow(image)[cite: 2]
plt.subplot(1, 3, 2)[cite: 2]
plt.title("Horizontal Mirror")
plt.imshow(horizontal)[cite: 2]
plt.subplot(1, 3, 3)[cite: 2]
plt.title("Vertical Mirror")
plt.imshow(vertical)[cite: 2]
plt.show()[cite: 2]
