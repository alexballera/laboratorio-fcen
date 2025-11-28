#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alex Ballera
https://docs.python.org/es/3.14/library/index.html
https://pandas.pydata.org/docs/reference/index.html
https://numpy.org/doc/stable/reference/index.html
https://docs.python.org/es/3.14/library/collections.html#
"""
# %% Importo las librerías
import numpy as np
import pandas as pd
from collections import Counter, defaultdict
# %% Ejercicio 1
def leer_parque(path, parque):
    df = pd.read_csv(path)

    arboles_df = df[df['espacio_ve'] == parque]
    
    # 3 formas de crear una lista de diccionarios a partir de un DataFrame de pandas
    # 1. https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html
    lista1 = arboles_df.to_dict(orient='records')
    
    columnas = arboles_df.columns
    lista2 = []
    
    # 2. construir dict usando las columnas y los valores de la fila
    for _, row in arboles_df.iterrows():
        registro = {col: row[col] for col in columnas}
        lista2.append(registro)
    
    # 3. construir dict usando las columnas y los valores de la fila
    lista3 = []
    i = 0
    
    for _, row in arboles_df.iterrows():
        registro = {}
        for item in row:
            registro[columnas[i]] = item
            i += 1
        lista3.append(registro)
        i = 0
    
    return lista1, lista2, lista3, df

# %% Ejercicio 2
def especies(lista_arboles):
    """Extrae el conjunto de especies únicas de la lista de árboles.
    
    Usa set comprehension para crear un conjunto sin duplicados.
    El acceso directo arbol['nombre_com'] asume que la clave existe.
    """
    arboles = set()
    
    # Set comprehension: crea un conjunto eliminando duplicados automáticamente
    arboles = {arbol['nombre_com'] for arbol in lista_arboles}

    return arboles
# %% Ejercicio 3
def contar_ejemplares(lista_arboles):
    """Cuenta la cantidad de ejemplares por especie.
    
    Devuelve 3 versiones del mismo resultado usando diferentes métodos.
    Todos usan .get() para acceso seguro evitando KeyError.
    
    .get(clave, default): busca 'clave' en el dict, si no existe devuelve 'default'
    """
    # Método 1: Counter (más eficiente y pythónico)
    # arbol.get('nombre_com') devuelve None si la clave no existe (evita KeyError)
    nombres = [arbol['nombre_com'] for arbol in lista_arboles if arbol.get('nombre_com')]
    result = dict(Counter(nombres))  # Counter cuenta automáticamente las ocurrencias
    
    # Método 2: dict con .get() para valores por defecto
    conteo = {}
    for arbol in lista_arboles:
        nombre = arbol.get('nombre_com')  # Devuelve None si no existe la clave
        if nombre:
            # conteo.get(nombre, 0) devuelve 0 si 'nombre' no está en conteo todavía
            conteo[nombre] = conteo.get(nombre, 0) + 1
    
    # Método 3: defaultdict (inicializa automáticamente con int() = 0)
    conteo2 = defaultdict(int)  # defaultdict(int) crea valores 0 automáticamente
    for arbol in lista_arboles:
        nombre = arbol.get('nombre_com')  # Acceso seguro, devuelve None si no existe
        if nombre:
            conteo2[nombre] += 1  # No necesita .get() porque defaultdict crea la clave
    conteo2 = dict(conteo2)  # Convertir de defaultdict a dict normal
        
    return result, conteo, conteo2

# %% Ejercicio 4
def obtener_altura(lista_arboles, especie):
    alturas = [float(arbol['altura_tot']) for arbol in lista_arboles if arbol.get('nombre_com') == especie]
        
    return alturas

def promedio(lista_numeros):
    return round(sum(lista_numeros) / len(lista_numeros), 2)

def maximo(lista_numeros):
    return round(max(lista_numeros), 2)

def promedios(path, parques, especie):
    medida = ['max', 'prom']
    maximos = []
    promedios = []
    medidas = []

    for parque in parques:
        lista_arboles = leer_parque(path, parque)[0]
        alturas = obtener_altura(lista_arboles, especie)

        maximos.append(maximo(alturas))
        promedios.append(promedio(alturas))

    medidas.append(maximos)
    medidas.append(promedios)
    
    df = pd.DataFrame(np.array(medidas), columns=parques, index=medida)

    return df

# %% Ejercicio 5
def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = [arbol['inclinacio'] for arbol in lista_arboles if arbol.get('nombre_com') == especie]
    return inclinaciones

# %% Ejercicio 6
def especimen_mas_inclinado(lista_arboles):
    inclinacion = 0
    for arbol in lista_arboles:
        if arbol['inclinacio'] >= inclinacion:
            especie = arbol['nombre_com']
            inclinacion = arbol['inclinacio']
        
    return especie, inclinacion

# %% Ejercicio 7
def especie_promedio_mas_inclinada(lista_arboles):
    arboles = {}
    especies = []
    for arbol in lista_arboles:
        arboles[arbol.get('nombre_com')] = obtener_inclinaciones(lista_arboles, arbol.get('nombre_com'))
    
    especies.append(arboles)
    
    especies_prom = []
    arboles = {}
    
    for k, v in especies[0].items():
        arboles[k] = promedio(v)
    especies_prom.append(arboles)
    
    inclinacion = 0
    for k, v in especies_prom[0].items():
        if v >= inclinacion:
            especie = k
            inclinacion = v
        
    return especie, inclinacion

# %%
# %% main
if __name__ == '__main__':
    especie = 'Jacarandá'
    path = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ministerio-de-espacio-publico-e-higiene-urbana/arbolado-espacios-verdes/arbolado-en-espacios-verdes.csv'
    path2 = '/home/alexballera/Documents/uba/laboratorio-fcen/clases/Clase-01-PythonPandas/practica/arbolado-en-espacios-verdes.csv'
    parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']

    # Ejercicio 1
    print('='*60)
    lista1, lista2, lista3, df = leer_parque(path2, parques[1])
    print(f"Ejercicio1: Árboles en {parques[0]}: {len(lista1)}\n")
    
    # Ejercicio 2
    print('='*60)
    arboles = especies(lista3)
    print(f"Ejercicio2: Especies en {parques[0]}: {len(arboles)}\n")
    
    # Ejercicio 3
    print('='*60)
    cantidad_especies = contar_ejemplares(lista1)
    # .get('Jacarandá', 0) busca la clave, si no existe devuelve 0 (evita KeyError)
    print(f"Ejercicio 3: Cant de {especie} = {cantidad_especies[0].get(especie, 0)}\n")
    
    # Ejercicio 4
    print('='*60)
    alturas = obtener_altura(lista2, especie)
    h_maximo = maximo(alturas)
    h_mean = promedio(alturas)
    print(f'Ejercicio 4: alturas de {especie}: {alturas} ')
    print(f'Ejercicio 4: máximo de {especie}: {h_maximo} ')
    print(f'Ejercicio 4: promedio de {especie}: {h_mean}\n ')
    
    proms = promedios(path2, parques, especie)
    print(f"""

Ejercicio 4:
Métricas {especie}:
              
    {proms} """)
    
    # Ejercicio 5
    print('='*60)
    inclinaciones = obtener_inclinaciones(lista1, especie)
    print(f'Ejercicio 5: inclinaciones de {especie}: {inclinaciones}\n')
    
    # Ejercicio 6
    print('='*60)
    especie, inclinacion = especimen_mas_inclinado(lista1)
    print(f'Ejercicio 6: Especie más inclinada: {especie}, inclinación: {inclinacion}\n')
    
    # Ejercicio 7
    print('='*60)
    especie, inclinacion = especie_promedio_mas_inclinada(lista1)
    print(f'Ejercicio 7: Especie más inclinada promedio: {especie}, inclinación: {inclinacion}\n')

# %%