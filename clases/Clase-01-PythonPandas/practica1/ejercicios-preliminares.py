#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alex Ballera
"""
# %% Importo las librerías
# %%
# Ejercicio 1
espesor = 0.11 # mm
h = 67.5 # metros
h *= 1000 # mm
dias = 1
h -= espesor

while h > 0:
    espesor *= 2
    h -= espesor
    dias += 1
    
print('dias', dias)
# %%
# Ejercicio 2
vocales = ['a', 'e', 'i', 'o', 'u']
silaba = {
    'a': 'pa',
    'e': 'pe',
    'i': 'pi',
    'o': 'po',
    'u': 'pu'
}

# for
def cadena_geringosa_for(palabra):
    palabra_geringosa = ''
    for letra in palabra:
        if letra in vocales:
            palabra_geringosa += letra + silaba[letra]
        else:
            palabra_geringosa += letra
    return 'for', palabra_geringosa

print(cadena_geringosa_for('Geringoso'))
# while
def cadena_geringosa_while(palabra):
    palabra_geringosa = ''
    long = len(palabra)
    i = 0
    while long > i:
        letra = palabra[i]
        if letra in vocales:
            palabra_geringosa += letra + silaba[letra]
        else:
            palabra_geringosa += letra
        i += 1
    return 'while', palabra_geringosa

print(cadena_geringosa_while('Geringoso'))
# %%
# Ejercicio 3
def pertenece(lista, elem):
    return len([item for item in lista if item == elem]) > 0

lista = ['a', 'b', 'c', 'd', 'e', 'f']
elem = 'h'

pertenece(lista, elem)
# %%
# Ejercicio 4
def mas_larga(lista1, lista2):
    return lista1 if len(lista1) > len(lista2) else lista2

lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,5,6]

mas_larga(lista1, lista2)
# %%
# Ejercicio 5
def rebotes():
    h = 100
    alturas = []
    i = 10
    while i > 0:
        h *= 3/5
        i -= 1
        alturas.append(round(h, 2))
    
    return alturas

rebotes()
# %%
# Ejercicio 6
def mezclar(cadena1, cadena2):
    mayor = cadena1 if len(cadena1) > len(cadena2) else cadena2
    menor = cadena2 if mayor == cadena1 else cadena1
    
    i = 0
    palabra = ''
    for letra in mayor:
        palabra += letra
        if len(menor) > i:
            palabra += menor[i]
            i += 1
    
    return palabra

mezclar('Josefa', 'Pepe')
# %%
# Ejercicio 7
t = 30
m = 12
TNA = 0.05
Monto = 500000
Cuota = 2684.11
# Monto total a pagar
TEM = TNA / m

# a.- Total a pagar
def total_pagar_a(cuota, t, m):
    return cuota * t * m
print(f'a.-Monto total a pagar {total_pagar_a(Cuota, t, m):.2f}')

# b.- 
monto_adicional = 1000
n = 12

def interes(monto, r):
    return monto * r


def capital(cuota, intereses):
    return cuota - intereses

def total_pagar_b(M, C, r):
    # año 1
    pago_acumulado = 0
    capital_acumulado = 0
    interes_acumulado = 0

    for i in range(12):
        cuota = monto_adicional + C
        intereses = interes(M, r)
        interes_acumulado += intereses
        capital_pagado = capital(cuota, intereses)
        capital_acumulado += capital_pagado
        M -= capital_pagado
        pago_acumulado = capital_acumulado

    # año 2 al 30
    for i in range(12*29):
        if M > 0:
            cuota = C
            intereses = interes(M, r)
            interes_acumulado += intereses
            capital_pagado = capital(cuota, intereses)
            capital_acumulado += capital_pagado
            M -= capital_pagado
            pago_acumulado = capital_acumulado + interes_acumulado
    
    return pago_acumulado

print(f'b.-Monto total a pagar {total_pagar_b(Monto, Cuota, TEM):.2f}')

# c.-
monto_extra = 1000
n = 4*m # años desde el año 6
inicio = 5*12
fin = inicio + n

def total_pagar_c(M, C, r, pago_extra_monto, pago_extra_mes_comienzo, pago_extra_mes_fin):
    # año 1
    pago_acumulado = 0
    capital_acumulado = 0
    interes_acumulado = 0
    meses = 0
    for i in range(pago_extra_mes_comienzo):
        cuota = Cuota
        intereses = interes(M, r)
        interes_acumulado += intereses
        capital_pagado = capital(cuota, intereses)
        capital_acumulado += capital_pagado
        M -= capital_pagado
        pago_acumulado = capital_acumulado
        meses += 1
        
    for i in range(pago_extra_mes_fin - pago_extra_mes_comienzo):
        cuota = Cuota + pago_extra_monto
        intereses = interes(M, r)
        interes_acumulado += intereses
        capital_pagado = capital(cuota, intereses)
        capital_acumulado += capital_pagado
        M -= capital_pagado
        pago_acumulado = capital_acumulado
        meses += 1
        
    for i in range(30*12 - pago_extra_mes_fin):
        if M > 0:
            cuota = C
            intereses = interes(M, r)
            interes_acumulado += intereses
            capital_pagado = capital(cuota, intereses)
            capital_acumulado += capital_pagado
            M -= capital_pagado
            pago_acumulado = capital_acumulado + interes_acumulado
            meses += 1
        
    return pago_acumulado, meses

totalc = total_pagar_c(Monto, Cuota, TEM, monto_extra, inicio, fin)

print(f'c.-Monto total a pagar {totalc[0]:.2f}')
print(f'c.-Meses requeridos {totalc[1]:.2f}')
# %%
def traductor_geringoso(lista: list):
    diccionario = {}
    
    for item in lista:
        diccionario[item] = cadena_geringosa_for(item)[1]
    return diccionario

lista = ['banana', 'manzana', 'mandarina']
print(traductor_geringoso(lista))