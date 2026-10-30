import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def rotateImage(image, degree):
    radian_deg = np.radians(degree)[cite: 2]
    cos_deg, sin_deg = np.cos(radian_deg), np.sin(radian_deg)[cite: 2]
    height, width = image.shape[:2][cite: 2]
    max_dim = int(np.sqrt(height**2 + width**2))[cite: 2]
    outputImage = np.zeros((max_dim, max_dim, 3), dtype=image.dtype)[cite: 2]

    centerY, centerX = max_dim // 2, max_dim // 2[cite: 2]

    for y in range(-height // 2, height // 2):[cite: 2]
        for x in range(-width // 2, width // 2):[cite: 2]
            newX = int(cos_deg * x - sin_deg * y) + centerX[cite: 2]
            newY = int(sin_deg * x + cos_deg * y) + centerY[cite: 2]
            if 0 <= newX < max_dim and 0 <= newY < max_dim:[cite: 2]
                outputImage[newY, newX] = image[y + height // 2, x + width // 2][cite: 2]
    return outputImage[cite: 2]

image = img.imread('D:/source.jpg')[cite: 2]
rotated_image = rotateImage(image, 45)[cite: 2]

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)[cite: 2]
plt.title("Original")
plt.imshow(image)[cite: 2]
plt.subplot(1, 2, 2)[cite: 2]
plt.title("Rotasi (Pusat)")
plt.imshow(rotated_image)[cite: 2]
plt.show()[cite: 2]
