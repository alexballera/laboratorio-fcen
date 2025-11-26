#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alex Ballera
"""
# %% Importo las librerías
import numpy as np
import pandas as pd
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
    arboles = set()
    
    arboles = {arbol['nombre_com'] for arbol in lista_arboles}

    return arboles
# %% Ejercicio 3

# %% Ejercicio 4

# %% Ejercicio 5

# %% Ejercicio 6

# %% main
if __name__ == '__main__':
    # Ejercicio 1
    path = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ministerio-de-espacio-publico-e-higiene-urbana/arbolado-espacios-verdes/arbolado-en-espacios-verdes.csv'
    path2 = '/home/alexballera/Documents/uba/laboratorio-fcen/clases/Clase-01-PythonPandas/practica/arbolado-en-espacios-verdes.csv'
    parque = 'GENERAL PAZ'
    lista1, lista2, lista3 = leer_parque(path, parque)
    print('='*40)
    print(f"Ejercicio1: Árboles en {parque}: {len(lista1)}")
    print(f'Lista en {parque}: {lista2}\n')
    
    # Ejercicio 2
    arboles = especies(lista3)
    print('='*40)
    print(f"Ejercicio2: Especies en {parque}: {len(arboles)}")
    print(f'arboles: {arboles}\n')
    
    # Ejercicio 3
    
    # Ejercicio 4
    
    # Ejercicio 5
    
    # Ejercicio 6

# %%