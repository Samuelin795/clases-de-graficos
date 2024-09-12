import matplotlib.pyplot as plt

# Definir los datos para el gráfico
x1 = [1, 4, 5]  # Valores del eje x
y1 = [2, 6, 3]   # Valores del eje y correspondientes

x2 = [5, 6, 7]
y2 = [3, 6, 3]
# Crear el gráfico
plt.figure(figsize=(8, 6))

# Dibujar la línea
plt.plot(x1, y1, label='Línea 1', color='b', marker='o', markersize=13, linestyle='-.')
plt.plot(x2, y2, label='Línea 2', color='r', marker='o', markersize=13, linestyle='-.')
# Configurar etiquetas y título
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Sample grathp')
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()