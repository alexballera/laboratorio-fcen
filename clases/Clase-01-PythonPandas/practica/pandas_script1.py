#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:22:23 2024

@author: mcerdeiro
"""

import pandas as pd
import numpy as np


#%% armo un dataframe a partir de un diccionario
d = {'nombre':['Antonio', 'Brenda', 'Camila', 'David', 'Esteban', 'Felicitas'], 'apellido': ['Restrepo', 'Saenz', 'Torres', 'Urondo', 'Valdes', 'Wainstein'], 'lu': ['78/23', '449/22', '111/24', '1/21', '201/06', '47/20'], 'nota1': [9, 7, 7, 4, 3, np.nan], 'nota2': [10, 6, 7, 8, 5, np.nan], 'aprueba': [True, True, True, False, False, np.nan]}

df = pd.DataFrame(data = d) # creamos un df a partir de un diccionario
df.set_index('lu', inplace = True) # seteamos una columna como index
#%%
df.head()   # primeras 5 líneas
df.tail()   # últimas 5
df.info()   # info del df
df.dtypes   # tipos de dato
df.columns  # columnas
df.index    # indice (id de filas, pueden no ser int)
df.describe()       # una descripción
df[['nombre', 'nota1']]     # selecciono algunas columnas (una lista) por nombre
df['nombre']        # solo una columna (sin lista) da una Serie
df.iloc[2]          # acceso a la fila i-ésima
df.iloc[2:6]        # filas 2 a 5
df.loc['78/23']     # acceso a fila por el index
df.loc['78/23', 'nombre']   # acceso a fila Y columna con index y nombre de col
df.sample()         # muestra una fila random
df.sample(n = 3)    # muestra n filas random
