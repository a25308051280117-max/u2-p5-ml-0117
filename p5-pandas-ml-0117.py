
import numpy as np
import pandas as pd

# Matias Lopez NC 0117

## datos
datos_alumno = [
    [100, 80, 10],
    [90, 70, 7],
    [120, 100, 14],
    [80, 50, 2]
]

# Poner nombre a las columnas
# y almacenar la tabla en la variable df DataFrame
df = pd.DataFrame(datos_alumno, columns=['ci', 'marcas', 'paquete'])
print(df)

# DATOS A PARTIR DE UN DICCIONARIO
alumno_diccionario = {
    "nombre": ["nicole", "matias", "alejandra", "ian", "cristian", "edgar"],
    "califa": [60, 90, 100, 80, 70, 50],
    "edad": [4, 15, 16, 16, 18, 14]
}

estudiante = pd.DataFrame(alumno_diccionario)
print(estudiante)

print("Matias Lopez NC 0117")
