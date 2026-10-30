import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def rotatePivotTopLeft(image, degree):
    radian = np.radians(degree)
    cos_deg, sin_deg = np.cos(radian), np.sin(radian)
    height, width = image.shape[:2]

    # Ukuran kanvas output untuk menampung citra hasil rotasi
    max_dim = int(np.sqrt(height**2 + width**2))
    output = np.zeros((max_dim, max_dim, 3), dtype=image.dtype)

    for y in range(height):
        for x in range(width):
            # Transformasi rotasi dengan pivot titik (0,0)[cite: 4]
            new_x = int(x * cos_deg - y * sin_deg)
            new_y = int(x * sin_deg + y * cos_deg)

            if 0 <= new_x < max_dim and 0 <= new_y < max_dim:
                output[new_y, new_x] = image[y, x]

    return output

image = img.imread('D:\\source.jpg')
rotated = rotatePivotTopLeft(image, 45)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image)
plt.subplot(1, 2, 2)
plt.title("Rotasi Pivot (0,0)")
plt.imshow(rotated)
plt.show()
