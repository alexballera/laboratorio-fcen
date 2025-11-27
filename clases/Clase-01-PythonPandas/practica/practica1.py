#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alex Ballera
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
    
    return lista1, lista2, lista3

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

# %% Ejercicio 5

# %% Ejercicio 6

# %% main
if __name__ == '__main__':
    # Ejercicio 1
    print('='*40)
    path = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ministerio-de-espacio-publico-e-higiene-urbana/arbolado-espacios-verdes/arbolado-en-espacios-verdes.csv'
    path2 = '/home/alexballera/Documents/uba/laboratorio-fcen/clases/Clase-01-PythonPandas/practica/arbolado-en-espacios-verdes.csv'
    parque = 'GENERAL PAZ'
    lista1, lista2, lista3 = leer_parque(path2, parque)
    print(f"Ejercicio1: Árboles en {parque}: {len(lista1)}")
    print(f'Lista en {parque}: {lista2}\n')
    
    # Ejercicio 2
    print('='*40)
    arboles = especies(lista3)
    print(f"Ejercicio2: Especies en {parque}: {len(arboles)}")
    print(f'arboles: {arboles}\n')
    
    # Ejercicio 3
    print('='*40)
    cantidad_especies = contar_ejemplares(lista1)
    print(f'Ejercicio3 {cantidad_especies}')
    # .get('Jacarandá', 0) busca la clave, si no existe devuelve 0 (evita KeyError)
    print(f"Jacarandá: {cantidad_especies[0].get('Jacarandá', 0)}")
    
    # Ejercicio 4
    
    # Ejercicio 5
    
    # Ejercicio 6

# %%