#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alex Ballera
"""
# %% Importo las librerías
import numpy as np
import pandas as pd
# %% Ejercicio 1
def leer_parque(path, nombre_archivo, parque):
    df = pd.read_csv(path + nombre_archivo)

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
    path = '/home/alexballera/Documents/uba/laboratorio-fcen/clases/Clase-01-PythonPandas/practica/'
    nombre_archivo = 'arbolado-en-espacios-verdes.csv'
    parque = 'GENERAL PAZ'
    lista1, lista2, lista3 = leer_parque(path, nombre_archivo, parque)
    print(f"Árboles en {parque}: {len(lista1)}")
    
    # Ejercicio 2
    arboles = especies(lista1)
    print(f"Especies en {parque}: {len(arboles)}")
    
    # Ejercicio 3
    
    # Ejercicio 4
    
    # Ejercicio 5
    
    # Ejercicio 6

# %%