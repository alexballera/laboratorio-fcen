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
    # creo DataFrame
    path = '/home/alexballera/Documents/uba/laboratorio-fcen/clases/Clase-01-PythonPandas/practica/'
    archivo = nombre_archivo
    df = pd.read_csv(path + archivo)

    arboles_df = df[df['espacio_ve'] == parque]

    df_grouped = arboles_df.groupby('nombre_cie')
    
    #for item in df_grouped.iterrows():
     #   print(item)

    return df_grouped, arboles_df
nombre_archivo = 'arbolado-en-espacios-verdes.csv'
parque = 'GENERAL PAZ'
df_grouped = leer_parque(nombre_archivo, parque)[0]
arboles_df = leer_parque(nombre_archivo, parque)[1]

# %%