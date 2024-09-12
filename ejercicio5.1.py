import numpy as np
from scipy.interpolate import interp1d

# Datos originales
x1_original = [1.0, 2.0, 3.0]
y1_original = [1.0, 4.0, 0.0]

# Crear un rango de valores para x1 en el intervalo deseado
x1_new = np.arange(0, 121, 5)  # De 0 a 120 con un intervalo de 5

# Interpolación lineal de los valores de y1
linear_interp = interp1d(x1_original, y1_original, kind='linear', fill_value='extrapolate')
y1_new = linear_interp(x1_new)

# Convertir arrays de numpy a listas si necesitas
x1_new_list = x1_new.tolist()
y1_new_list = y1_new.tolist()

# Imprimir los datos
print("x1_new:", x1_new_list)
print("y1_new:", y1_new_list)

# Si deseas guardar en un archivo CSV
import csv

# Guardar en un archivo CSV
with open('datos_interpolados.csv', 'w', newline='') as csvfile:
    fieldnames = ['x1', 'y1']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for x, y in zip(x1_new_list, y1_new_list):
        writer.writerow({'x1': x, 'y1': y})
