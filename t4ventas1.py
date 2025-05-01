# Importación de librerías
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Lectura del archivo CSV
datos_ventas = pd.read_csv("ventas.csv", encoding='utf-8')

# Mostrar el DataFrame original
print("Datos originales:")
print(datos_ventas)

# Agregar columna de Ventas Totales (Unidades Vendidas * Precio Unitario)
datos_ventas['Ventas Totales'] = datos_ventas['Unidades Vendidas'] * datos_ventas['Precio Unitario']

print("\nDatos con Ventas Totales:")
print(datos_ventas)

# Gráfica de barras 
colores = ['#D7F2BA', '#BDE4A8', '#9CC69B', '#79B4A9', '#676F54']
plt.bar(datos_ventas['Producto'], datos_ventas['Unidades Vendidas'], color=colores)
plt.title('Unidades Vendidas por Producto')
plt.xlabel('Producto')
plt.ylabel('Unidades Vendidas')
plt.grid(axis='y')
plt.show()

# Gráfico de pastel 
plt.pie(datos_ventas['Unidades Vendidas'],
        labels=datos_ventas['Producto'],
        autopct='%1.1f%%',
        colors=colores,
        startangle=90)
plt.title('Proporción de Unidades Vendidas por Producto')
plt.axis('equal')  # Hace que el pastel se vea redondo
plt.show()
