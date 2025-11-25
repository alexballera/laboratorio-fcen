#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alex Ballera
"""
# %% Importo las librerías
import numpy as np
import pandas as pd
# %% Ejercicio 1
def leer_parque(nombre_archivo, parque):
    path = '/home/alexballera/Documents/uba/laboratorio-fcen/clases/Clase-01-PythonPandas/practica/'
    archivo = nombre_archivo
    df = pd.read_csv(path + archivo)

    arboles_df = df[df['espacio_ve'] == parque]
    
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html
    dict = arboles_df.to_dict(orient='records')
    
    lista = []
    for _, row in arboles_df.iterrows():
        # construir dict usando las columnas y los valores de la fila
        registro = {col: row[col] for col in arboles_df.columns}
        lista.append(registro)
    
    columnas = arboles_df.columns
    lista2 = []
    arbol = {}
    i = 0
    
    for _, row in arboles_df.iterrows():
        for item in row:
            arbol[columnas[i]] = item
            i += 1
        arbol_copy = arbol.copy()
        lista2.append(arbol_copy)
        i = 0

    return dict, lista, lista2


if __name__ == '__main__':
    nombre_archivo = 'arbolado-en-espacios-verdes.csv'
    parque = 'GENERAL PAZ'
    dict, lista, lista2 = leer_parque(nombre_archivo, parque)
    print(f"Árboles en {parque}: {len(lista)}")

# %%