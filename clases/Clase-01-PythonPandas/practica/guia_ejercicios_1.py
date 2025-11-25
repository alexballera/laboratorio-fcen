# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:32:31 2025

@author: ICBC
"""
import pandas as pd
import numpy as np

nombre_archivo = 'arbolado-en-espacios-verdes.csv'
parque = 'CENTENARIO'
especie = 'Jacarandá'

# Ejercicio 1
def leer_parque(nombre_archivo, parque):
    df = pd.read_csv(nombre_archivo)
    
    arboles = df[df['espacio_ve'] == parque]
    
    columnas = arboles.columns
    informacion = []
    arbol = {}
    i = 0
    
    for _, row in arboles.iterrows():
        for item in row:
            arbol[columnas[i]] = item
            i += 1
        arbol_copy = arbol.copy()
        informacion.append(arbol_copy)
        i = 0

    return informacion

lista_arboles = leer_parque(nombre_archivo, parque)

# Ejercicio 2
def especies(arboles):
    nombre_com = set()
    
    for item in arboles:
        nombre_com.add(item['nombre_com'])

    return nombre_com

nombre_com = especies(lista_arboles)

# Ejercicio 3
def contar_ejemplares(arboles):
    especies = []
    
    for arbol in arboles:
        especies.append(arbol['nombre_com'])
    
    result = {i:especies.count(i) for i in especies}

    return result
    
contar_ejemplar = contar_ejemplares(lista_arboles)

# Ejercicio 4
def obtener_alturas(lista_arboles, especie):
    h = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            h.append(float(arbol['altura_tot']))
    maximo = max(h)
    prom = round(np.mean(h).tolist(), 2)
    
    return maximo, prom
    
max_prom = obtener_alturas(lista_arboles, especie)

# Ejercicio 5
def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinaciones.append(int(arbol['inclinacio']))
    

    return inclinaciones[0]

inclinaciones = obtener_inclinaciones(lista_arboles, especie)

# Ejercicio 6
def especimen_mas_inclinado(lista_arboles):
    nombre = ""
    inc = 0
    
    for arbol in lista_arboles:
        if arbol['inclinacio'] >= inc:
            nombre = arbol['nombre_com']
            inc = arbol['inclinacio']
     
    return nombre, inc

especimen_mas_inclinado = especimen_mas_inclinado(lista_arboles)