import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Definir las fechas para el eje X
# Por simplicidad, comenzaremos en una fecha de referencia y agregaremos días
start_date = datetime(2016, 10, 3)  # Fecha de inicio
x_dates = [start_date + timedelta(days=int(day)) for day in [1.0, 2.0, 3.0, 4.0]]

# Datos del eje Y correspondientes
y1 = [1.0, 4.0, 4.0, 0.0]

# Crear el gráfico
plt.figure(figsize=(10, 6))

# Dibujar la línea
plt.plot(x_dates, y1, label='Línea 1', color='b', marker='o')

# Configurar el formato de fechas en el eje X
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

# Configurar etiquetas y título
plt.xlabel('Fecha')
plt.ylabel('Eje Y')
plt.title('Gráfico con Fechas en el Eje X')
plt.legend()

# Rotar las etiquetas de las fechas para mejor visualización
plt.gcf().autofmt_xdate()

# Mostrar el gráfico
plt.grid(True)
plt.show()
