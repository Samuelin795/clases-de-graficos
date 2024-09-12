import matplotlib.pyplot as plt

# Definir los datos para el gráfico
x1 = [1.0, 2.0, 3.0]  # Valores del eje x
y1 = [1.0, 4.0, 0.0]   # Valores del eje y correspondientes


# Crear el gráfico
plt.figure(figsize=(8, 6))

# Dibujar la línea
plt.plot(x1, y1, label='Línea 1', color='b', marker='o')

# Configurar etiquetas y título
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Sample grathp')
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()
