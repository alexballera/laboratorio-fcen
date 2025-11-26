#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:23:11 2024

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
df.columns  # columnas, The column labels of the DataFrame
df.index    # indice (id de filas, pueden no ser int)
df[['nombre', 'nota1']]     # selecciono algunas columnas (una lista) por nombre
df['nombre']        # solo una columna (sin lista) da una Serie
df.describe()       # una descripción
df.iloc[2]          # acceso a la fila i-ésima
df.iloc[2:6]        # filas 2 a 5
df.loc['78/23']     # acceso a fila por el index
df.loc['78/23', 'nombre']   # acceso a fila Y columna con index y nombre de col
df.sample()         # muestra una fila random
df.sample(n = 3)    # muestra n filas random

#%% manejo de valores NaN

df.isna()       # Detect missing values.
df.isnull()     # is an alias for isna
df.notna()      # Detect existing (non-missing) values
df.notnull()    # is an alias for notna
df.dropna()     # Remove missing values https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna
df.dropna(axis='columns')   # Drop the columns where at least one element is missing
df.dropna(how='all')        # solo si TODA la fila es nula
df.dropna(thresh=3)         # solo si tiene muy pocos campos (trhesh) no-nan, Keep only the rows with at least 3 non-NA values
df.dropna(subset=['nombre', 'apellido'])    # Define in which columns to look for missing values.
df.dropna(subset=['nota1', 'apellido'])
df.fillna(0)    # Fill NA/NaN values using the specified method, o por el valor pasado como parámetro

values = {"nota1": 0, "nota2": 0, "aprueba": False}
df.fillna(value=values) # reemplaza NA/NaN por los valores pasados como parámetros

#%% ordenar por alguna columna 
df.sort_values(by= 'nombre', ascending = True)

#%% modificar una o varias entradas
df
df.loc['1/21', 'nombre'] = 'Daniel' # modifico la entrada accediendo a la ubicación por fila (index) y columna (nombre de la columna) y defino el nuevo valor con '='
df.replace({'nombre': {'David': 'Daniel'}}) # modifico todas las apariciones de David
df

### OJO - un caso es inplace, el otro no.

df.replace(7, 8)
df.replace({7: 8, 3: 2})
df.replace({'nota2': {7: 9, 5: 6}})
df.astype({'nota2': 'float'})  # cambio de tipo

#%% modificar nombres de las columnas
df.rename(columns={"nota1": "Parcial1", "nota2": "Parcial2"})


#%% calcular promedio y otras cosas
# .agg Aggregate using one or more operations over the specified axis
df
df.agg('min')
df[['nota1', 'nota2']].agg(['sum', 'min', 'max', 'mean'])

df['promedio'] = (df['nota1'] + df['nota2'])/2
df['promedio'] = df[['nota1', 'nota2']].agg('mean', axis='columns')
df

#%%
df.all() # solo para variables booleanas (OJO --> si no es bool es todo es True salvo el caso vacío) Return whether all elements are True, potentially over an axis
df.any() # Return whether any element is True, potentially over an axis
df.isna()
df.isna().all()
df.isna().any()

df['aprueba'].all()
df['aprueba'].any()

#%% otros "drop" - eliminar partes del df
df
df.drop(['78/23'], axis = 0) # se elimina la fila con index = 78/23

df.drop(['apellido', 'nombre'], axis = 1) # tiro las columnas apellido y nombre

df.duplicated() # dice True en las filas que están duplicadas (luego de la primera aparición)

df.duplicated(keep=False) # dice True en las filas que están duplicadas (incluyendo la primera aparición)

df.duplicated(subset=['nota1'])

df.duplicated(subset=['nota1'], keep = False)

df.drop_duplicates()  # Return DataFrame with duplicate rows removed

df.drop_duplicates(subset=['nota1'])

df.drop_duplicates(subset=['nota1'], keep = 'last')

#%% chequear condiciones
# Get Equal to of dataframe and other, element-wise (binary operator eq).
# Among flexible wrappers (eq, ne, le, lt, ge, gt) to comparison operators.
# Equivalent to ==, !=, <=, <, >=, > with support to choose axis (rows or columns) and level for comparison

df == 7
df.eq(7) # Get Equal to of dataframe and other, element-wise (binary operator eq)

df!= 7
df.ne(7) # Get Not equal to of dataframe and other, element-wise (binary operator ne)

df[['nota1', 'nota2']] <= 7
df[['nota1', 'nota2']].le(7) # Get Less than or equal to of dataframe and other, element-wise (binary operator le)

df[['nota1', 'nota2']] >= 7
df[['nota1', 'nota2']].ge(7) # Get Greater than or equal to of dataframe and other, element-wise (binary operator ge)

df[['nota1', 'nota2']] > 7
df[['nota1', 'nota2']].gt(7) # Get Greater than of dataframe and other, element-wise (binary operator gt)

df.isin([6, 7]) # Whether each element in the DataFrame is contained in values.
~df.isin([6, 7]) # To check if values is not in the DataFrame, use the ~ operator
df.isin({'nota1': [6,7]}) # When values is a dict, we can pass values to check for each column separately

#%% otras funciones aplicables al df

df.eval('nota_final = nota1 + 1') # Evaluate a string describing operations on DataFrame columns.
df.eval('promedio = 0.5*nota1 + 0.5*nota2')


df.map(lambda x: len(str(x))) # Apply a function to a Dataframe elementwise, defino la funcion acá mismo con lambda
df[['nombre']].map(lambda x: x.upper())
df[['nota1']].map(lambda x: x*10)

# puedo armar la función aparte o dentro del map con lambda
def f(x):
    res = x+1
    return res

df[['nota1']].map(f)
df[['nota1']].map(lambda x: x + 1)


df[['nota1', 'nota2']].transform(lambda x: x*10) # Call func on self producing a DataFrame with the same axis shape as self
#%% iterar sobre las filas
df.iterrows() # Iterate over DataFrame rows as (index, Series) pairs.

for e in df.iterrows():
    print(e)

for i, e in df.iterrows():
    print(i, e['nombre'])

df.itertuples() # Iterate over DataFrame rows as namedtuples

for e in df.itertuples():
    print(e)
    
for e in df.itertuples():
    print(e.nombre)

for e in df.itertuples():
    print(e.Index)
    
lista_ingresantes_pandemia = []
for e in df.itertuples():
    ingreso = int(e.Index.split('/')[1])
    if ingreso in [20, 21]:
        lista_ingresantes_pandemia.append((e.nombre, e.apellido))

lista_dfitems = []
for label, content in df.items():
    print(f'label: {label}')
    print(f'content: {content}', sep='\n')
    lista_dfitems.append((label, content))
#%% concatenar con otro dataframe
d2 = {'nombre':['Gregoria', 'Horacio'], 'apellido': ['Pérez', 'Quirno'], 'lu': ['09/23', '657/21'], 'nota1': [2,10], 'nota2': [7, 8], 'aprueba': [False, True]}

df_nuevo = pd.DataFrame(data = d2)
df_nuevo.set_index('lu', inplace = True)
pd.concat([df, df_nuevo]) # Concatenate pandas objects along a particular axis

#%% merge equivalente a SQL JOIN
df1 = pd.DataFrame({'a': ['foo', 'bar'], 'b': [1, 2]})
df2 = pd.DataFrame({'a': ['foo', 'baz'], 'c': [3, 4]})

df1.merge(df2, how='inner', on='a') # SQL INNER JOIN
df1.merge(df2, how='left', on='a') # SQL LEFT OUTER JOIN
df1.merge(df2, how='right', on='a') # SQL RIGHT OUTER JOIN
df1.merge(df2, how='cross') # SQL CROSS JOIN

df1.join(df2.set_index('a'), how='inner', on='a') # SQL INNER JOIN
df1.join(df2.set_index('a'), how='left', on='a') # SQL LEFT OUTER JOIN
df1.join(df2.set_index('a'), how='right', on='a') # SQL RIGHT OUTER JOIN
df1.join(df2.set_index('a'), how='cross') # SQL CROSS JOIN
df1.join(df2.set_index('a'), how='outer') # SQL OUTER JOIN

#%% armar una copia
df_copia = df.copy()
#%% guardar el dataframe como archivo csv

df.to_csv('planilla')


#%% FILTROS

df['nota1']>=7 # nos da una serie booleana, que indica donde se cumple la condición
# el index de esta serie es el del df

(df['nota1']>=7).sum()

df[df['nota1']>=7] # nos da el sub-dataframe donde se cumple la condición

df[ (df['nota1']>=7) & (df['nota2']>=7)]

df[ df['nota1']== 7]

df[ df['nota1'].isin([7,4])] # Whether each element in the DataFrame is contained in values.

df[(df['nota2'] <=7) & df['aprueba']]

df[(df['nota2'] <=7) | df['aprueba']]

# filter: Subset the dataframe rows or columns according to the specified index labels.
# Note that this routine does not filter a dataframe on its contents. The filter is applied to the labels of the index.

filtro = pd.DataFrame(np.array(([1, 2, 3], [4, 5, 6])),
                  index=['mouse', 'rabbit'],
                  columns=['uno', 'dos', 'tres'])

filtro.filter(items = ['uno', 'dos'])
filtro.filter(regex = 'o$', axis=1) # select columns by regular expression axis=1
filtro.filter(like = 'ra', axis=0) # select rows containing 'ra'

#%% otras cosas
a = df.to_numpy() # Convert the DataFrame to a NumPy array; con tipos mixtos no; 

d = df[['nota1', 'nota2']].dropna().to_numpy()

df['nota1']
df['nota1'].unique() # Return unique values based on a hash table. Uniques are returned in order of appearance. This does NOT sort.

df['nota1'].value_counts() # Return a Series containing the frequency of each distinct row in the Dataframe.
df['nota1'].value_counts(dropna = False) # incluye valores nulos
df
df.where(df['nota1'] > 6, 0) # donde no es mayor a 6 pongo 0

#%%
iris = pd.read_csv('https://raw.githubusercontent.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/iris.csv')
pd.plotting.andrews_curves(iris, 'Name')  
