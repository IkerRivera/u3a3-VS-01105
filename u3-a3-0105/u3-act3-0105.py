from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import cv2

## Iker Montoya 0105
print("Iker Montoya 0105")
print("UIII Act3 Importación y descripción de datos con Pandas ML")

MI_Imagen = cv2.imread("leopardito.jpg")
plt.imshow(MI_Imagen)
plt.title("Leopardito XD")
plt.show()

print("+--+-+-+-+-+-+-+-+-+- puntos en la imagen +-+-++-+-+-+-+-+-+-+-+-+-")

plt.imshow(MI_Imagen)
x = [100, 100, 300, 600]
y = [100, 400, 500, 600]
plt.scatter(x, y, s=20, c="red")
plt.show()

print("+--+-+-+-+-+-+-+-+-+- Cuadro en la imagen +-+-++-+-+-+-+-+-+-+-+-+-")

MI_Imagen = cv2.imread("leopardito.jpg")
plt.imshow(MI_Imagen)

x = [100, 100, 500, 500, 100]
y = [500, 100, 100, 500, 500]
plt.plot(x, y, c="blue")
plt.show()

print("+--+-+-+-+-+-+-+-+-+- Circulo verde en la imagen +-+-++-+-+-+-+-+-+-+-+-+-")

plt.imshow(MI_Imagen)
circulo = plt.Circle((300, 300), 100, color="green", fill=False, linewidth=3)
plt.gca().add_patch(circulo)
plt.show()

print("Iker Montoya")