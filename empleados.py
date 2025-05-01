import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Arreglo de productividad semanal
productividad = np.array([75, 80, 90, 85, 70])
print("Promedio de productividad:", np.mean(productividad))
print("Máximo valor de productividad:", np.max(productividad))

# Leer archivo CSV
empleados = pd.read_csv("empleados.csv", encoding='utf-8')

# Filtrar empleados del departamento Ventas
ventas = empleados[empleados['Departamento'] == 'Ventas']
print("\nEmpleados del departamento Ventas:")
print(ventas['Nombre'])

# Agregar columna Bono (10% del salario)
empleados['Bono'] = empleados['Salario'] * 0.10

# Mostrar DataFrame con bono
print("\nEmpleados con bono:")
print(empleados)

# Gráfica de barras
plt.figure(figsize=(10, 6))
plt.bar(empleados['Nombre'], empleados['Salario'], color='#68A691')
plt.title('Salario por Empleado')
plt.xlabel('Nombre')
plt.ylabel('Salario')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y')
plt.show()
