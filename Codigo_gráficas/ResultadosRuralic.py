#Analizar las necesidades y resultados de las encuestas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

archivo = "RuralicEncuestas.csv"
df = pd.read_csv(archivo, header=None)

# Asignar nombres a las columnas
headers = ["Conoce la norma NSR-10", "Zona del País", "Ciudad-Municipio", "Tipo Vivienda", "No. Habitaciones",
           "No. Personas", "Adquirió vivienda", "Condiciones Vivienda", "Mejoras Necesarias", "Preocupación Construcción",
           "Acceso Internet", "Implementar Software", "Características Software", "Utilizado Software", "Resistencia Vivienda",
           "Desafios Viviendas", "Obstáculos Construir", "Utiliza Herramientas digitales", "Usaría Ruralic", 
           "Apoyo Construcción", "Programas Alcaldías", "Otras Características Software"]
df.columns = headers
#print (df.head())

mejoras_count = df['Mejoras Necesarias'].value_counts()
mejoras_percentage = (mejoras_count / mejoras_count.sum()) * 100

# Crear un DataFrame para mostrar resultados
resultados_mejoras = pd.DataFrame({
    'Respuesta': mejoras_count.index,
    'Frecuencia': mejoras_count.values,
    'Porcentaje': round(mejoras_percentage, 2)
})


preocupacion = df['Preocupación Construcción'].value_counts()
preocupacion_percentage = (preocupacion / preocupacion.sum()) * 100
resultados_preocupacion = pd.DataFrame({
    'Respuesta': preocupacion.index,
    'Frecuencia': preocupacion.values,
    'Porcentaje': round(preocupacion_percentage, 2)
})
print(resultados_preocupacion)

desafio = df['Desafios Viviendas'].value_counts()
desafio_percentage = (desafio / desafio.sum()) * 100
resultados_desafio = pd.DataFrame({
    'Respuesta': desafio.index,
    'Frecuencia': desafio.values,
    'Porcentaje': round(desafio_percentage, 2)
})
print(resultados_desafio)

# 12,13,19,22
implementar = df['Implementar Software'].value_counts()
implementar_percentage = (implementar / implementar.sum()) * 100
resultados_implementar = pd.DataFrame({
    'Respuesta': implementar.index,
    'Frecuencia': implementar.values,
    'Porcentaje': round(implementar_percentage, 2)
})
print(resultados_implementar)

caracteristicas = df['Características Software'].value_counts()
caracteristicas_percentage = (caracteristicas / caracteristicas.sum()) * 100
resultados_caracteristicas = pd.DataFrame({
    'Respuesta': caracteristicas.index,
    'Frecuencia': caracteristicas.values,
    'Porcentaje': round(caracteristicas_percentage, 2)
})
print (resultados_caracteristicas)

ruralic = df['Usaría Ruralic'].value_counts()
ruralic_percentage = (ruralic / ruralic.sum()) * 100
resultados_ruralic = pd.DataFrame({
    'Respuesta': ruralic.index,
    'Frecuencia': ruralic.values,
    'Porcentaje': round(ruralic_percentage, 2)
})
print (resultados_ruralic)

software = df['Otras Características Software'].value_counts()
software_percentage = (software / software.sum()) * 100
resultados_software = pd.DataFrame({
    'Respuesta': software.index,
    'Frecuencia': software.values,
    'Porcentaje': round(software_percentage, 2)
})
print (resultados_software)
zona = df['Zona del País'].value_counts()
zona_percentage = (zona / zona.sum()) * 100
resultados_zona = pd.DataFrame({
    'Respuesta': zona.index,
    'Frecuencia': zona.values,
    'Porcentaje': round(zona_percentage, 2)
})
print (resultados_zona)