import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import splrep, splev

# Definir los datos para el gráfico
x = [0, 1, 2, 3]  # Valores del eje x
y = [0, 10, 25, 50]  # Valores del eje y correspondientes

# Ajustar spline cúbico
spl = splrep(x, y, s=0)  # s=0 para ajuste exacto
x_smooth = np.linspace(min(x), max(x), 500)
y_smooth = splev(x_smooth, spl)

# Datos para la primera línea adicional (lineal)
x_line1 = [0, 3]
y_line1 = [0, 10]

# Datos para la segunda línea adicional (parabólica)
x_parabola = np.linspace(0, 3, 500)
y_parabola = 30 * (x_parabola ** 2) - 30 * x_parabola + 10  # Ejemplo de función parabólica

# Crear el gráfico
plt.figure(figsize=(10, 6))

# Dibujar la curva suave
plt.plot(x_smooth, y_smooth, label='Curva Suave con Spline Cúbico', color='b')

# Dibujar la primera línea adicional
plt.plot(x_line1, y_line1, label='Línea Recta Adicional', color='g', linestyle='--')

# Dibujar la segunda línea adicional
plt.plot(x_parabola, y_parabola, label='Curva Parabólica', color='orange', marker='s', markersize=5, linestyle='-')

# Dibujar los puntos originales
plt.plot(x, y, 'o', color='r', label='Puntos Originales')

# Configurar etiquetas y título
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Curva Suave con Spline Cúbico y Líneas Adicionales')
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()
