import numpy as np
import imageio as img
import matplotlib.pyplot as plt

def zoomPlus(image, factor):
    height, width = image.shape[:2][cite: 3]
    new_height = int(height / factor)[cite: 3]
    new_width = int(width / factor)[cite: 3]
    imgZoom = np.zeros((new_height, new_width, 3), dtype=image.dtype)[cite: 3]

    for y in range(new_height):[cite: 3]
        for x in range(new_width):[cite: 3]
            ori_y = int(y * factor)[cite: 3]
            ori_x = int(x * factor)[cite: 3]
            ori_y = min(ori_y, height - 1)[cite: 3]
            ori_x = min(ori_x, width - 1)[cite: 3]
            imgZoom[y, x] = image[ori_y, ori_x][cite: 3]

    return imgZoom[cite: 3]

image = img.imread('D:\\source.jpg')[cite: 3]
skala = 2.0[cite: 3]
imgZoom = zoomPlus(image, skala)[cite: 3]

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)[cite: 3]
plt.title("Original")
plt.imshow(image)[cite: 3]
plt.subplot(1, 2, 2)[cite: 3]
plt.title("Zoom Plus")
plt.imshow(imgZoom)[cite: 3]
plt.show()[cite: 3]
