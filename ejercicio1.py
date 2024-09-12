import matplotlib.pyplot as plt

# Definir los datos para el gráfico
x = [0, 3.0]  # Valores del eje x
y = [0, 140]   # Valores del eje y correspondientes

# Crear el gráfico
plt.figure(figsize=(140, 6))

# Dibujar la línea
plt.plot(x, y, label='Línea hasta 140', color='b', marker='o')

# Configurar etiquetas y título
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Sample grathp')
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()
