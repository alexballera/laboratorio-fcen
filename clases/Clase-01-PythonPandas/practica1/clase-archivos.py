#%%
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 21:49:35 2025

@author: Admin
"""
#%%
import csv
path = 'g:\\Mi unidad\\educacion\\uba\\exactas\\lab-datos\\clases\\Clase-01-PythonPandas\\practica01\\'
# Archivos .txt
name = 'datame.txt'
#%%
f = open(name, 'rt')
data = f.read()
f.close()
#%%
with open(path + name, 'rt') as file:
    data_nuevo = file.read()
#%%
# Se agrega texto al inicio y fin
data_nuevo = 'Texto agregado al inicio\n' + data
data_nuevo = data_nuevo + 'Texto agregado al final!!!'
#%%
# Escribir archivo
nuevo_archivo = open('datame_modificado.txt', 'w')
nuevo_archivo.write(data_nuevo)
nuevo_archivo.close()

# Archivos .csv
nombre = 'cronograma_sugerido.csv'
with open(nombre, 'rt') as file:
    materias = []
    next(file)
    for line in file:
        linea = line.split(',')
        materias.append(linea[1])
        
f = open(nombre)
filas = csv.reader(f)
materias2 = []
next(f)
for fila in filas:
    materias2.append(fila[1])
f.close()
    