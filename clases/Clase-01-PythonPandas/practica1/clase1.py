#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alex Ballera
"""
# %% importar librerías
import math
import csv
import random
# %% Copias
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
# %% math
print(math.sqrt(2))
print(math.exp(2))
print(math.cos(120))
print(math.log(8))
print(math.factorial(5))
print(math.gcd(48, 18))
# %% Manejo de archivos
ruta = './'
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
# %% Ejercicio 1
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
# %% verificar opciones
def verificar_opciones(numeros):
    num = sorted(numeros)
    if (num[0] == num[-1]):
        print('Generala')
    
    elif (num[0] == num[-2]):
        print('Poker')
        
    elif (num[-1] == num[-2]):
        print('Full')
    
    elif escalera(numeros):
        print('Escalera')
    
    else:
        print('Ninguno')

    return numeros
    
verificar_opciones(tirar_dados())
# %% datame.txt
'''
Escribir un programa que recorra las líneas del archivo ‘datame.txt’
e imprima solamente las líneas que contienen la palabra ‘estudiante’
'''
path = './'
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
'''
Utilizando el archivo cronograma_sugerido , armar una lista de las
materias del cronograma, llamada “lista_materias 
'''
nombre_archivo = 'cronograma_sugerido.csv'
# %% “cuantas_materias(n)”
'''
Luego, definir una función “cuantas_materias (n)” que, dado un
número de cuatrimestre (n entre 3 y 8), devuelva la cantidad de
materias a cursar en ese cuatrimestre. Por ejemplo:
cuantas_materias(5) debe devolver 3.
'''

# %%