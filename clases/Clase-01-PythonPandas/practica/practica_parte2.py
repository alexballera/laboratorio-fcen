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
# %% preparacion_df
def preparacion_df(path):
    arboles_veredas = pd.read_csv(path)
    df = pd.DataFrame(arboles_veredas)
    
    data_arboles_veredas = df[['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho']]
    return data_arboles_veredas, df

# %% ejercicio 8
def parques_veredas_df():
    arboles = df[['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol', 'ancho_acera']]
    vereda = arboles[arboles['ancho_acera'] > '0']
    parque = arboles[arboles['ancho_acera'].isna()]
    
    vereda = vereda[['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol']]
    parque = parque[['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol']]

    return parque, vereda # df_tipas_parques, df_tipas_veredas,
# %% main
if __name__ == '__main__':
    path1 = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/atencion-ciudadana/arbolado-publico-lineal/arbolado-publico-lineal-2017-2018.csv'
    path2 = '/home/alexballera/Documents/uba/laboratorio-fcen/clases/Clase-01-PythonPandas/practica/arbolado-publico-lineal-2017-2018.csv'
    especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
    
    # preparacion_df
    data_arboles_veredas, df = preparacion_df(path2)

    # Ejercicio 8
    print('='*60)
    df_tipas_parques, df_tipas_veredas = parques_veredas_df()

# %%