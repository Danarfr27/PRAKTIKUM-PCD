import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

def Translasi(image, shiftX, shiftY):
    imgTranslasi = np.roll(image, shift=shiftY, axis=0) # Geser vertikal[cite: 1]
    imgTranslasi = np.roll(imgTranslasi, shift=shiftX, axis=1) # Geser horizontal[cite: 1]

    # Mengisi bagian yang kosong dengan warna hitam[cite: 1]
    if shiftY > 0:
        imgTranslasi[:shiftY, :] = 0 # Bagian atas jika geser ke bawah[cite: 1]
    elif shiftY < 0:
        imgTranslasi[shiftY:, :] = 0 # Bagian bawah jika geser ke atas[cite: 1]

    if shiftX > 0:
        imgTranslasi[:, :shiftX] = 0 # Bagian kiri jika geser ke kanan[cite: 1]
    elif shiftX < 0:
        imgTranslasi[:, shiftX:] = 0 # Bagian kanan jika geser ke kiri[cite: 1]

    return imgTranslasi

image = img.imread("D:/source.jpg")[cite: 1]
imgResult = Translasi(image, shiftX=50, shiftY=-300)[cite: 1]

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image)[cite: 1]
plt.subplot(1, 2, 2)
plt.title("Hasil Translasi")
plt.imshow(imgResult)[cite: 1]
plt.show()[cite: 1]
