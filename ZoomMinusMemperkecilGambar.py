import numpy as np
import imageio as img
import matplotlib.pyplot as plt

def zoomMinus(image, factor):
    height, width = image.shape[:2]
    # Menghitung dimensi baru yang diperkecil berdasarkan faktor skala[cite: 4]
    new_height = int(height * factor)
    new_width = int(width * factor)
    imgZoomOut = np.zeros((new_height, new_width, 3), dtype=image.dtype)

    for y in range(new_height):
        for x in range(new_width):
            ori_y = int(y / factor)
            ori_x = int(x / factor)
            ori_y = min(ori_y, height - 1)
            ori_x = min(ori_x, width - 1)
            imgZoomOut[y, x] = image[ori_y, ori_x]

    return imgZoomOut

image = img.imread('D:\\source.jpg')
skala_perkecil = 0.5  # Memperkecil dimensi gambar menjadi 50%[cite: 4]
imgSmall = zoomMinus(image, skala_perkecil)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title(f"Original ({image.shape[1]}x{image.shape[0]})")
plt.imshow(image)
plt.subplot(1, 2, 2)
plt.title(f"Zoom Minus ({imgSmall.shape[1]}x{imgSmall.shape[0]})")
plt.imshow(imgSmall)
plt.show()
