#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alex Ballera
"""
# %% importar librerías
import math
import csv
import random
import numpy as np
import pandas as pd
# %% 
# =============================================
# Copias
# =============================================
a = [1, 2, 3, 4, 5]
b = a  # Copia por referencia
c = a.copy()  # Copia por valor
d = a[:]  # Copia por valor
print("Lista original a:", a)
print("Copia por referencia b:", b)
print("Copia por valor c:", c)
print("Copia por valor d:", d)
# %%
print("Antes de modificar a:")
print(b == a)
print(b is a)
print(c == a)
print(c is a)
# %%
a.append(6)
print("Después de modificar a:")
print("Lista original a:", a)
print("Copia por referencia b:", b)
print("Copia por valor c:", c)
print("Copia por valor d:", d)
# %%
# =============================================
# Módulos
# =============================================
print(math.sqrt(2))
print(math.exp(2))
print(math.cos(120))
print(math.log(8))
print(math.factorial(5))
print(math.gcd(48, 18))
# %%
# =============================================
# Manejo de archivos
# =============================================
ruta = '/home/alexballera/Documents/uba/laboratorio-fcen/clases/Clase-01-PythonPandas/practica1/'
nombre_archivo = 'datame.txt'
f = open(ruta + nombre_archivo, 'rt')
data = f.read()
f.close()
print(data)
# %%
with open(ruta + nombre_archivo, 'rt') as f:
    data = f.read()
print(data)
# %%
data_nuevo = 'Línea nueva\n \nOtra línea nueva\n\n' + data
data_nuevo = data_nuevo + '\nÚltima línea nueva\n'

datame = open('datame_modificado.txt', 'w')
datame.write(data_nuevo)
datame.close()
# %%
nombre_archivo = 'cronograma_sugerido.csv'
with open(ruta + nombre_archivo, 'rt') as file:
    for line in file:
        datos_linea = line.split(',')
        print(datos_linea[0])
# %%
f = open(ruta + nombre_archivo, 'rt')
lineas = csv.reader(f)
encabezado = next(f)
print('Encabezado', encabezado)

for linea in lineas:
    print(linea)
f.close()
# %%
# =============================================
# Ejercicio 1
# =============================================
'''
Escribir una función generala_tirar()  que simule una tirada de dados
para el juego de la generala. Es decir, debe devolver una lista aleatoria
de 5 valores de dados. Por ejemplo [2,3,2,1,6]
'''
# %% tirar dados
def tirar_dados():
    return [random.randint(1,6) for i in range(1,6)]

tirar_dados()    
# %% escalera
def escalera(numeros):
    return numeros == [1,2,3,4,5] or numeros == [2,3,4,5,6]

def generala(num):
    return num[0] == num[-1]

def poker (num):
    return num[0] == num[-2]

def full(num):
    return (num[-1] == num[-2] and num[0] == num[1] == num[2]) or (num[-1] == num[-2] == num[-3] and num[0] == num[1])
# %% verificar opciones
def verificar_opciones(numeros):
    num = sorted(numeros)
    if (generala(num)):
        print('Generala')
    
    elif (poker(num)):
        print('Poker')
        
    elif (full(num)):
        print('Full')
    
    elif escalera(numeros):
        print('Escalera')
    
    else:
        print('Ninguno')

    return numeros
    
verificar_opciones(tirar_dados())
# %%
# =============================================
# Ejercicio 2
# =============================================
'''
Escribir un programa que recorra las líneas del archivo ‘datame.txt’
e imprima solamente las líneas que contienen la palabra ‘estudiante’
'''
path = ruta
name = 'datame.txt'
file = open(path + name, 'rt')

data = [line for line in file.readlines() if 'estudiante' in line]

datame_estudiante = ''
for line in data:
    datame_estudiante += line

nuevo_doc = open('datame_estudiante.txt', 'w')
nuevo_doc.write(datame_estudiante)
nuevo_doc.close()

# %%
# =============================================
# Ejercicio 3
# =============================================
'''
Utilizando el archivo cronograma_sugerido , armar una lista de las
materias del cronograma, llamada “lista_materias 
'''
name = 'cronograma_sugerido.csv'
file = open(path + name, 'rt')
lineas = csv.reader(file)
header = next(file)

lista_materias = [linea[1] for linea in lineas]
print(lista_materias)
# %% “cuantas_materias(n)”
'''
Luego, definir una función “cuantas_materias (n)” que, dado un
número de cuatrimestre (n entre 3 y 8), devuelva la cantidad de
materias a cursar en ese cuatrimestre. Por ejemplo:
cuantas_materias(5) debe devolver 3.
'''
def cuantas_materias(n):
    if not (3 <= n <= 8):
        print('Debe introducir un cuatrimestre entre 3 y 8, ambos inclusive')
        return
    
    name = 'cronograma_sugerido.csv'
    file = open(path + name, 'rt')
    next(file)
    lineas = csv.reader(file)
    lista_materias = [linea[1] for linea in lineas if linea[0] == str(n)]

    return len(lista_materias)

cuantas_materias(5)
# %% materias_cuatrimestre(nombre_archivo, n)
'''
Definir una función materias_cuatrimestre(nombre_archivo, n) que recorra el
archivo indicado, conteniendo información de un cronograma sugerido de cursada,
y devuelva una lista de diccionarios con la información de las materias sugeridas
para cursar el n-ésimo cuatrimestre.
'''
# diccionario de diccionarios
def materias_cuatrimestre(nombre_archivo, n):
    if not (3 <= n <= 8):
        return 'Debe introducir un cuatrimestre entre 3 y 8, ambos inclusive'

    
    file = open(path + nombre_archivo, 'rt')
    reader = csv.reader(file)
    next(reader)
    materias = {}
    i = 0
    for row in reader:
        if row[0] == str(n):
            i += 1
            materias[f'materia_sugerida_{i}'] = {'asignatura': row[1], 'correlatividad': row[2]}
            
    return materias
    
materias_cuatrimestre('cronograma_sugerido.csv', 3)
# %% lista de diccionarios
def materias_cuatrimestre2(nombre_archivo, n):
    if not (3 <= n <= 8):
        return 'Debe introducir un cuatrimestre entre 3 y 8, ambos inclusive'
    
    materias = []
    with open(path + nombre_archivo, 'rt') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row[0] == str(n):
                materia = dict(zip(header, row))
                materias.append(materia)
    
    return materias

materias_cuatrimestre2('cronograma_sugerido.csv', 3)
# %%
# =============================================
# NUMPY
# =============================================
# rangos
print(np.arange(4))
print(np.arange(2, 9, 2))
print(np.linspace(0, 10, 10))
# %% arrays 
# concatenar
a = np.array([1, 2, 3, 4])
b = np.array([5,6,7,8])
np.concat((a, b))
np.concatenate((a, b))
x = np.array([[1,2], [3,4]])
y = np.array([[5,6], [7,8]])
z = np.concat((x,y), axis = 0)
print('concat axis=0', z)

z = np.concat((x,y), axis=1)
print("concat axis=1", z)
# %%
arr = np.array([
    [[0,1,2,3], [4,5,6,7]],
    [[3,8,10,-1], [0,1,1,0]],
    [[3,3,3,3], [5,5,5,5]]
])
print(f'dimensiones: {arr.ndim}')
print(f'elementos por eje: {arr.shape}')
print(f'total entradas, tamaño = 3*2*4 = {arr.size}')
print(f'reshape, modifico la forma a 12*2: {arr.reshape((12,2))}')
print(f'reshape, modifico la forma a 4*6: {arr.reshape((4,6))}')
print(f'reshape, modifico la forma a 3* lo que corresponda: {arr.reshape((3,-1))}')

# %%
# ARRAYS SIMPLES UNIDIMENSIONAL
data = np.array([1,2])
ones = np.ones(2)
zeros = np.zeros(2)
print(data)
print(ones)
print(zeros)
# %%
# operaciones
# Suma
suma = data + ones
print(f'Suma     : {data} + {ones} = {suma}')

# Resta
resta = data - ones
print(f'Resta    : {data} - {ones} = {resta}')

# Multiplicación
mult = data * data
print(f'Mult     : {data} * {data} = {mult}')

# Multiplicación escalar
mult = data * 1.6
print(f'Mult Esc : {data} * 1.6 = {mult}')

# División
div = data / data
print(f'División : {data} / {data} = {div}')
# %% 
# max, min, sum
# max, devuelve el valor máximo del array
data = np.array([1,3,5])
max = data.max()
print(f'Máximo {data} = {max}')

# min, devuelve el valor mínimo del array
min = data.min()
print(f'Mínimo {data} = {min}')

# sum, devuelve la suma del array
sum = data.sum()
print(f'Suma {data} = {sum}') 

# %% 
# ARRAYS MULTIDIMENSIONAL
data = np.array([[1,2], [3,4], [5,6]])
print(data)
print(f'shape {data.shape}')

# %%
# Obtener celdas
print(data[0,1]) # celda row 0 col 1
print(data[1:3]) # rows del 1 al 3 (sin incluir al 3) = del 1 al 2
print(data[0:2,0]) # rows del 0 al 1 y col 0

# %%
# Operaciones
# max
max = data.max()
print(f'Máximo: {max}')

# min
min = data.min()
print(f'Mínimo: {min}')

# sum
sum = data.sum()
print(f'Suma: {sum}')
# %%
# max/min ejes "y" o cols, axis = 0, devuelve el máximo/mínimo de cada columna
max_axis_0 = data.max(axis = 0)
print(max_axis_0)
# %%
# max/min ejes "x" o rows, axis = 1, devuelve el máximo/mínimo de cada fila
max_axis_1 = data.max(axis = 1)
print(max_axis_1)
# %%
# sum ejes "y" o cols, axis = 0, devuelve la suma de cada columna (suma vertical)
sum_axis_0 = data.sum(axis = 0)
print(sum_axis_0)
# %%
# sum ejes "x" o rows, axis = 1, devuelve la suma de cada línea (suma horizontal)
sum_axis_1 = data.sum(axis = 1)
print(sum_axis_1)
# %% ---------------------------------------------------
# Ejercicio
def pisar_elemento(M, e):
    M_new = []
    for row in M:
        row_new = []
        if e in row:
            for num in row:
                if num == e:
                    row_new.append(-1)
                else:
                    row_new.append(int(num))
            M_new.append(row_new)
        else:
            M_new.append(row.tolist())
    M = np.array(M_new)
    return M

M = np.array([
    [0,1,2,3],
    [2,5,6,7]
])
e = 2
print(pisar_elemento(M, e))
# %%
# =============================================
# PANDAS: Series & DataFrames
# =============================================
# %%