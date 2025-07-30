#Analizar y graficar los resultados obtenidos de la encuesta

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

archivo = "RuralicEncuestas.csv"
df = pd.read_csv(archivo, header = None)
#print (df.head(5))
headers = ["Conoce la norma NSR-10","Zona del País","Ciudad-Municipio","Tipo Vivienda","No. Habitaciones",
           "No. Personas","Adquirió vivienda","Condiciones Vivienda","Mejoras Necesarias","Preocupación Construcción",
           "Acceso Internet","Implementar Software","Características Software","Utilizado Software","Resistencia Vivienda",
           "Desafios Viviendas","Obstáculos Construir","Utiliza Herramientas digitales","Usaría Ruralic","Apoyo Construcción",
           "Programas Alcaldías","Otras Características Software"]
df.columns = headers
df.columns
#print(headers)

#print(df.describe())
sns.set_theme(style="darkgrid")
# ===== Pregunta 1. ¿Conoce la normatividad de sismo-resistencia (NSR 10) para la construcción de viviendas en Colombia?====
rta_NSR_10 = df['Conoce la norma NSR-10'].value_counts()

total_respuestas = rta_NSR_10.sum()
porcentajes = (rta_NSR_10 / total_respuestas) * 100

plt.figure(figsize=(7,6))
ax = sns.barplot(x=rta_NSR_10.index, y=rta_NSR_10.values, palette="BuGn", hue=rta_NSR_10.index, legend=False)
for i, value in enumerate(rta_NSR_10.values):
     plt.text(i, value + 0.5, f'{porcentajes.iloc[i]:.1f}%', ha='center')

plt.title("¿Conoce la normatividad de sismo-resistencia (NSR 10)?")
plt.xlabel("Respuesta")
plt.ylabel("Cantidad")
plt.show() 

# ===== Pregunta 2 ¿En qué zona del país vive? =====

zona = df['Zona del País'].value_counts()

total_respuestas = zona.sum()
porcentajes = (zona / total_respuestas) * 100

plt.figure(figsize=(7,6))
ax = sns.barplot(x=zona.index, y=zona.values, palette="Blues_d", hue=zona.index, legend=False)
for i, value in enumerate(zona.values):
     plt.text(i, value + 0.5, f'{porcentajes.iloc[i]:.1f}%', ha='center')

plt.title("¿En qué zona del país vive?")
plt.xlabel("Zona del País")
plt.ylabel("Porcentaje (%)")
plt.show() 

# ===== Pregunta 3 ¿En cual ciudad o municipio reside? ======  
ciudad_counts = df['Ciudad-Municipio'].value_counts().reset_index()
ciudad_counts.columns = ['Ciudad-Municipio', 'frecuencia']

total_respuestas = ciudad_counts['frecuencia'].sum()

ciudad_counts['porcentaje'] = (ciudad_counts['frecuencia'] / total_respuestas) * 100

plt.figure(figsize=(12, 8))
bar_plot = sns.barplot(data=ciudad_counts, x='porcentaje', y='Ciudad-Municipio', palette='crest', legend=False)

plt.title('¿En cuál ciudad o municipio reside?')
plt.xlabel('Porcentaje')
plt.ylabel('Ciudad-Municipio')

for index, row in ciudad_counts.iterrows():
    bar_plot.text(row['porcentaje'], index, f'{row["porcentaje"]:.1f}%', color='black')
plt.show()

# ======= Pregunta 4 ¿En qué Tipo Vivienda reside actualmente? =======

vivienda_counts = df['Tipo Vivienda'].value_counts().reset_index()
vivienda_counts.columns = ['Tipo Vivienda', 'frecuencia']
total_respuestas = vivienda_counts['frecuencia'].sum()
vivienda_counts['porcentaje'] = (vivienda_counts['frecuencia'] / total_respuestas) * 100

plt.figure(figsize=(8, 5))
wedges, texts, autotexts = plt.pie(
    vivienda_counts['frecuencia'],
    autopct='%1.1f%%',
    startangle=90,
    colors=sns.color_palette("BuGn", n_colors=len(vivienda_counts)),
    wedgeprops=dict(edgecolor='w'),
    textprops={'fontsize': 8},
    pctdistance=0.7
)
plt.legend(
    wedges, vivienda_counts['Tipo Vivienda'],
    title="Tipo de Vivienda",
    loc="center left",  
    bbox_to_anchor=(0.7, -0.4, 0.3, 0.9)
)
plt.title('¿En qué Tipo Vivienda reside actualmente?', pad=15,fontweight='bold')
plt.axis('equal')
plt.show()
# === Pregunta 5 ¿Cuántas habitaciones tiene su vivienda? ===

rta_habitaciones = df['No. Habitaciones'].value_counts(normalize=True) * 100
plt.figure(figsize=(8, 6))
ax = sns.displot(df, x="No. Habitaciones", discrete=True, kde=False, color="skyblue")
for i, value in enumerate(rta_habitaciones.index):
    total = rta_habitaciones[value]
    count = df['No. Habitaciones'].value_counts()[value]
    plt.text(value - 0.10, count + 0.4, f'{total:.1f}%', ha='left', fontsize=12)   
plt.xticks([1, 2, 3])
# Configuración de la gráfica
plt.title("¿Cuántas habitaciones tiene su vivienda?",fontweight='bold')
plt.xlabel("Número de Habitaciones")
plt.ylabel("Cantidad ")
plt.show()

# === Pregunta 6 ¿Cuántas personas viven en su hogar? ===

rta_no_personas = df['No. Personas'].value_counts()
plt.figure(figsize=(8, 6))
colors = sns.color_palette("ch:s=.25,rot=-.25", n_colors=len(rta_no_personas))
wedges, texts, autotexts = plt.pie(rta_no_personas,  autopct='%1.1f%%', startangle=90, colors=colors)
centro_circulo = plt.Circle((0,0), 0.70, color='#E1EFF0')
plt.gca().add_artist(centro_circulo)
plt.legend(
    wedges, 
    rta_no_personas.index,  
    title="No. Personas",
    loc="center left",  
    bbox_to_anchor=(0.9, 0.7) 
)
plt.title("¿Cuántas personas viven en su hogar?", fontweight="bold")
plt.show()

# === Pregunta 7 ¿Cómo adquirió su vivienda? ===
rta_adquisicion = df['Adquirió vivienda'].value_counts()
porcentajes = (rta_adquisicion / rta_adquisicion.sum()) * 100

plt.figure(figsize=(8, 6))
sns.barplot(x=porcentajes.index, y=porcentajes.values, palette=sns.color_palette("flare", as_cmap=False))

for i, porcentaje in enumerate(porcentajes.values):
    plt.text(i, porcentaje + 0.5, f'{porcentaje:.1f}%', ha='center', fontweight='bold')
plt.title("¿Cómo adquirió su vivienda?", fontweight="bold")
plt.ylabel("Porcentaje")
plt.show()

# === Pregunta 8  ¿Cómo describe las condiciones de su vivienda? ===

rta_condiciones = df["Condiciones Vivienda"].value_counts()
porce = (rta_condiciones / rta_condiciones.sum()) * 100
nueva_etiquetas = [label.replace(" ", "\n") for label in rta_condiciones.index]
plt.figure(figsize=(8, 6))
plt.gca().set_facecolor('#F5F5DC')
colors = sns.color_palette("ch:s=.25,rot=-.25", n_colors=len(rta_condiciones))
plt.stem(rta_condiciones.index, rta_condiciones.values, linefmt='-', markerfmt='o', basefmt=" ")
plt.scatter(rta_condiciones.index, rta_condiciones.values, color=colors, s=100, zorder=2)

for i, porcen in enumerate(porce):
    plt.text(i, rta_condiciones.values[i] + 0.5, f'{porcen:.1f}%', ha='center', fontweight='bold')

plt.title("¿Cómo describe las condiciones de su vivienda?", fontweight="bold")
plt.ylabel("Frecuencia")
plt.xticks(ticks=range(len(nueva_etiquetas)), labels=nueva_etiquetas, rotation=0, ha='center')
plt.grid(visible=True, color='gray', linestyle='--', linewidth=0.5)
plt.show()

# === Pregunta 9 ¿Qué tipo de mejoras considera necesarias para su vivienda?==

rta_Mejoras = df["Mejoras Necesarias"].value_counts().reset_index()
rta_Mejoras.columns = ['Mejoras Necesarias', 'frecuencia']
total_respuestas = rta_Mejoras['frecuencia'].sum()
rta_Mejoras['porcentaje'] = (rta_Mejoras['frecuencia'] / total_respuestas) * 100
plt.figure(figsize=(8, 6))
wedges, texts, autotexts = plt.pie(
    rta_Mejoras['frecuencia'],
    autopct='%1.1f%%',
    startangle=90,
    colors=sns.color_palette("PRGn", n_colors=len(rta_Mejoras)),
    wedgeprops=dict(edgecolor='w'),
    textprops={'fontsize': 8,'fontweight': 'bold'},
    pctdistance=0.7
)
plt.legend(
    wedges, rta_Mejoras['Mejoras Necesarias'],
    loc="center left",  
    bbox_to_anchor=(0.1, -0.5, 0.4, 0.9)
)
plt.title('¿Qué tipo de mejoras considera necesarias para su vivienda?', pad=15,fontweight='bold')
plt.axis('equal')
plt.show()
# === Pregunta 10 ¿Cuál es su principal preocupación con respecto a la construcción de su vivienda?
rta_preocupacion = df['Preocupación Construcción'].value_counts()
total_respuestas = rta_preocupacion.sum()
porcentajes = (rta_preocupacion / total_respuestas) * 100
plt.figure(figsize=(7,6))
ax = sns.barplot(x=rta_preocupacion.index, y=rta_preocupacion.values, palette="Spectral", hue=rta_preocupacion.index, legend=False)
for i, value in enumerate(rta_preocupacion):
     plt.text(i, value + 0.5, f'{porcentajes.iloc[i]:.1f}%', ha='center')
labels = [
    "Cumplimiento de normativas\nde sismo-resistencia", 
    "Optimización de costos\ny recursos", 
    "Acceso a\nhabitaciones seguras", 
]
plt.xticks(ticks=range(len(labels)), labels=labels)
plt.title("¿Cuál es su principal preocupación con respecto a la construcción de su vivienda?",fontweight='bold')
plt.xlabel("Respuesta")
plt.ylabel("Cantidad")
plt.show()

# ===Pregunta 11 ¿Tiene acceso a internet en su hogar?===
internet = df['Acceso Internet'].value_counts().reset_index()
internet.columns = ['Acceso Internet', 'frecuencia']
total_respuestas = internet['frecuencia'].sum()
internet['porcentaje'] = (internet['frecuencia'] / total_respuestas) * 100
plt.figure(figsize=(8, 5))
wedges, texts, autotexts = plt.pie(
    internet['frecuencia'],
    autopct='%1.1f%%',
    startangle=90,
    colors=sns.color_palette("YlGnBu", n_colors=len(internet)),
    wedgeprops=dict(edgecolor='w'),
    textprops={'fontsize': 12},
    pctdistance=0.7
)
plt.legend(
    wedges, internet['Acceso Internet'],
    title="Internet",
    loc="center left",  
    bbox_to_anchor=(0.7, -0.4, 0.3, 0.9)
)
plt.title('¿Tiene acceso a internet en su hogar?', pad=15,fontweight='bold')
plt.axis('equal')
plt.show()
# === Pregunta 12 ¿Consideraría implementar un software 
# que facilite el diseño de viviendas seguras, optimizando recursos y cumpliendo con la normativa de sismo-resistencia?
software = df["Implementar Software"].value_counts()
total = software.sum()
percentages = (software / total) * 100
plt.figure(figsize=(8, 7))
ax = sns.histplot(x=df["Implementar Software"], discrete=True, shrink=0.5, stat="percent", legend=False)

for i, (value, percentage) in enumerate(zip(software, percentages)):
    plt.text(i, value + 0.3, f'{percentage:.1f}%', ha='center',va='top',color="w")
plt.title("¿Consideraría implementar un software\nque facilite el diseño de viviendas seguras\noptimizando recursos\n y cumpliento con la normativa de sismo-resistencia?")
plt.ylabel("Porcentaje")
plt.show()

# === Pregunta 13 ¿Cuáles serían las principales características que valoraría en un software de este tipo?
carac_sw = df['Características Software'].value_counts()
total_respuestas = carac_sw.sum()
porcentajes = (carac_sw / total_respuestas) * 100
plt.figure(figsize=(7,10))
ax = sns.barplot(x=carac_sw.index, y=carac_sw.values, palette="Spectral", hue=carac_sw.index, legend=False)
for i, value in enumerate(carac_sw.values):
     plt.text(i, value + 0.5, f'{porcentajes.iloc[i]:.1f}%', ha='center')
labels = [
    "Todas las\nanteriores",
    "Fácil de usar\ne intuitivo", 
    "Cálculo preciso\nde materiales", 
    "Cumplimiento\nde normativas",
    "Reducción\nde costos",
]
plt.xticks(ticks=range(len(labels)), labels=labels)
plt.title("¿Cuáles serían las principales características\nque valoraría en un software de este tipo?",fontweight="bold",pad=15)
plt.xlabel("Respuesta")
plt.ylabel("Cantidad")
plt.show()

# == Pregunta 14 ¿Alguna vez ha utilizado un software para la mejora de su vivienda?""
software = df['Utilizado Software'].value_counts()
plt.figure(figsize=(8, 6))
colors = sns.color_palette("blend:#7AB,#EDA", n_colors=len(software))
wedges, texts, autotexts = plt.pie(software,  autopct='%1.1f%%', startangle=90, colors=colors)
centro_circulo = plt.Circle((0,0), 0.70, color='#FDFFB6')
plt.gca().add_artist(centro_circulo)
plt.legend(
    wedges, 
    software.index,  
    title="Ha utilizado Software",
    loc="center left",  
    bbox_to_anchor=(0.9, 0.7) 
)
plt.title("¿Alguna vez ha utilizado un software\npara la mejora de su vivienda?", fontweight="bold")
plt.show()

# Pregunta 15 ¿Qué tan seguro se siente con respecto a la resistencia de su vivienda ante desastres naturales?
resistencia = df['Resistencia Vivienda'].value_counts().reset_index()
resistencia.columns = ['Resistencia Vivienda', 'frecuencia']
total_respuestas = resistencia['frecuencia'].sum()
resistencia['porcentaje'] = (resistencia['frecuencia'] / total_respuestas) * 100
plt.figure(figsize=(12, 8))
bar_plot = sns.barplot(data=resistencia, x='porcentaje', y='Resistencia Vivienda', palette="dark:#5A9_r", legend=False, width=0.6)
plt.title('¿Qué tan seguro se siente con respecto a la resistencia de su vivienda ante desastres naturales?',fontweight="bold")
plt.xlabel('Cantidad')
plt.ylabel('Resistencia')

for index, row in resistencia.iterrows():
    bar_plot.text(row['porcentaje'], index, f'{row["porcentaje"]:.1f}%', color='black')
plt.show()

# Pregunta 16 ¿Cuál es el mayor desafío que enfrenta en términos de vivienda?

desafios = df['Desafios Viviendas'].value_counts().reset_index()
desafios.columns = ['Desafios Viviendas', 'frecuencia']
desafios_filtrado = desafios[desafios['Desafios Viviendas'] != 'Opción 4']
total_respuestas = desafios_filtrado['frecuencia'].sum()
desafios_filtrado['porcentaje'] = (desafios_filtrado['frecuencia'] / total_respuestas) * 100
def split_label(label, max_words=3):
    words = label.split()
    return '\n'.join([' '.join(words[i:i + max_words]) for i in range(0, len(words), max_words)])
plt.figure(figsize=(12, 10))
bar_plot = sns.barplot(data=desafios_filtrado, y='porcentaje', x='Desafios Viviendas', palette='RdYlBu', legend=False)
plt.title('¿Cuál es el mayor desafío que enfrenta en términos de vivienda?', fontweight='bold')
plt.ylabel('Porcentaje')
plt.xlabel('Desafíos de Vivienda')
for index, row in desafios_filtrado.iterrows():
    bar_plot.text(
        row['Desafios Viviendas'],
        row['porcentaje'] + 0.5,
        f'{row["porcentaje"]:.1f}%',
        color='black',
        ha='center'
    )
labels = [split_label(label.get_text(), max_words=3) for label in bar_plot.get_xticklabels()]
bar_plot.set_xticklabels(labels)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Pregunta 17 ¿Cuáles cree que son los principales obstáculos para construir vivienda segura y eficiente en su comunidad?
construir = df['Obstáculos Construir'].value_counts()
plt.figure(figsize=(8, 6))
colors = sns.color_palette("Oranges", n_colors=len(construir))
wedges, texts, autotexts = plt.pie(construir,  autopct='%1.1f%%', startangle=90, colors=colors,pctdistance=0.7,textprops={'fontsize': 8})
centro_circulo = plt.Circle((0,0), 0.50, color='#f6bc66')
plt.gca().add_artist(centro_circulo)
plt.legend(
    wedges, 
    construir.index,  
    loc="center left",  
    bbox_to_anchor=(-0.3, -0.4, 0.2, 0.9) 
)
plt.title("¿Cuáles cree que son los principales obstáculos\npara construir vivienda segura y eficiente en su comunidad?", fontweight="bold")
plt.show()

# Pregunta 18 ¿Utiliza actualmente alguna herramienta digital para el diseño y cálculo de proyectos?
herramientas = df['Utiliza Herramientas digitales'].value_counts()
total_respuestas = herramientas.sum()
porcentajes = (herramientas / total_respuestas) * 100

plt.figure(figsize=(7,6))
ax = sns.barplot(x=herramientas.index, y=herramientas.values, palette="crest", hue=herramientas.index, legend=False)
for i, value in enumerate(herramientas.values):
    plt.text(i, value + 0.5, f'{porcentajes.iloc[i]:.1f}%', ha='center')

plt.title("¿Utiliza actualmente alguna herramienta\ndigital para el diseño y cálculo de proyectos?",fontweight="bold")
plt.xlabel("Respuesta")
plt.ylabel("Cantidad")
plt.show()

# Pregunta 19 ¿Cuál es la motivación para utilizar el software Ruralic?
ruralic = df["Usaría Ruralic"].value_counts() 
porce = (ruralic / ruralic.sum()) * 100

def ajustar_etiquetas(etiqueta):
    palabras = etiqueta.split()
    return '\n'.join([' '.join(palabras[i:i+2]) for i in range(0, len(palabras), 2)])
nueva_etiquetas = [ajustar_etiquetas(label) for label in ruralic.index]
plt.figure(figsize=(8, 7))
plt.gca().set_facecolor('#f2f5ff')
colors = sns.color_palette("flare", n_colors=len(ruralic))

plt.stem(ruralic.index, ruralic.values, linefmt='-', markerfmt='o', basefmt=" ") #Gráfico de Tallo
plt.scatter(ruralic.index, ruralic.values, color=colors, s=100, zorder=3)

for i, porcen in enumerate(porce):
    plt.text(i, ruralic.values[i] + 1.0, f'{porcen:.1f}%', ha='center', fontweight="bold")

plt.title("¿Porque Usaría Ruralic?", fontweight="bold")
plt.ylabel("Frecuencia")
plt.xticks(ticks=range(len(nueva_etiquetas)), labels=nueva_etiquetas, rotation=0, ha='center')
plt.grid(visible=True, color='purple', linestyle='--', linewidth=0.8)
plt.show()

# Pregunta 20  ¿Qué tipo de apoyo consideraría más útil para la construcción de su vivienda?
apoyo = df['Apoyo Construcción'].value_counts()
total_respuestas = apoyo.sum()
porcentajes = (apoyo / total_respuestas) * 100
def ajustar_etiquetas(etiqueta):
    palabras = etiqueta.split()
    return '\n'.join([' '.join(palabras[i:i+1]) for i in range(0, len(palabras), 2)])
nueva_etiquetas = [ajustar_etiquetas(label) for label in apoyo.index]

plt.figure(figsize=(7,7))
ax = sns.barplot(x=apoyo.index, y=apoyo.values, palette="YlGn", hue=apoyo.index, legend=False)
for i, value in enumerate(apoyo.values):
     plt.text(i, value + 0.5, f'{porcentajes.iloc[i]:.1f}%', ha='center')

plt.title("¿Qué tipo de apoyo consideraría\nmás útil para la construcción de su vivienda?",fontweight ="bold")
plt.xlabel("Respuesta")
plt.xticks(ticks=range(len(nueva_etiquetas)), labels=nueva_etiquetas, rotation=0, ha='center')
plt.ylabel("Cantidad")
plt.show()

# Pregunta 21 ¿Cómo evalúa el impacto de los programas actuales de las alcaldías en su comunidad?
alcaldias = df['Programas Alcaldías'].value_counts()
plt.figure(figsize=(8, 6))
colors = sns.color_palette("mako", n_colors=len(alcaldias))
wedges, texts, autotexts = plt.pie(alcaldias,  autopct='%1.1f%%', startangle=90, colors=colors,pctdistance=0.7,textprops={'fontsize': 8})
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
centro_circulo = plt.Circle((0,0), 0.50, color='#caffbf')
plt.gca().add_artist(centro_circulo)
plt.legend(
    wedges, 
    alcaldias.index,  
    loc="center left",  
    bbox_to_anchor=(-0.3, -0.4, 0.2, 0.9) 
)
plt.title("¿Cómo evalúa el impacto de los \nprogramas actuales de las alcaldías en su comunidad?", fontweight="bold")
plt.show()

# Pregunta 22 ¿Qué características adicionales le gustaría ver en un software de diseño y planificación de viviendas?
otras_car = df["Otras Características Software"].value_counts().reset_index()
otras_car.columns = ['Otras Características Software', 'frecuencia']
total_respuestas = otras_car['frecuencia'].sum()
otras_car['porcentaje'] = (otras_car['frecuencia'] / total_respuestas) * 100
plt.figure(figsize=(8, 6))
wedges, texts, autotexts = plt.pie(
    otras_car['frecuencia'],
    autopct='%1.1f%%',
    startangle=90,
    colors=sns.color_palette("viridis", n_colors=len(otras_car)),
    wedgeprops=dict(edgecolor='w'),
    textprops={'fontsize': 8,'fontweight': 'bold','color':'w'},
    pctdistance=0.7
)
plt.legend(
    wedges, otras_car['Otras Características Software'],
    loc="center left",  
    bbox_to_anchor=(0.1, -0.5, 0.4, 0.9)
)
plt.title('¿Qué características adicionales le gustaría\nver en un software de diseño y planificación de viviendas?', pad=15,fontweight='bold')
plt.axis('equal')
plt.show()