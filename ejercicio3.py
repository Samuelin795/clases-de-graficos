import matplotlib.pyplot as plt

# Definir los datos para el gráfico
x1 = [10, 20, 30]  # Valores del eje x
y1 = [20, 40, 00]   # Valores del eje y correspondientes

x2 = [10, 20, 30]
y2 = [40, 10, 30]
# Crear el gráfico
plt.figure(figsize=(8, 6))

# Dibujar la línea
plt.plot(x1, y1, label='Línea 1', color='b', marker='o')
plt.plot(x2, y2, label='Línea 2', color='r', marker='o')
# Configurar etiquetas y título
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Sample grathp')
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()