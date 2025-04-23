import matplotlib.pyplot as plt

# Datos simulados (temperatura en °C cada hora)
tiempo = [1, 2, 3, 4, 5, 6, 7, 8]  # Horas
temperatura = [22.1, 22.5, 23.0, 24.2, 25.0, 24.8, 24.3, 23.9]  # °C

# Crear el gráfico
plt.plot(tiempo, temperatura, marker='o', color='blue', linestyle='--')

# Añadir título y etiquetas
plt.title('Temperatura Registrada por el Sensor')
plt.xlabel('Hora')
plt.ylabel('Temperatura (°C)')

# Mostrar cuadrícula
plt.grid(True)

# Mostrar el gráfico
plt.show()