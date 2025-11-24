# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 16:40:50 2025

@author: Admin
"""

def format_number(num):
    return round(num, 2)

# Ejercicio 1
# ¿Cuánto tiempo pasa antes de que la pila de billetes sea más alta que el obelisco?
def cuanto_tiempo():
    espesor = 0.11
    h = 67500
    sumador = espesor
    i = 0
    
    while sumador < h:
        sumador += espesor * 2 * i
        i += 1
    dias = i - 1

    return dias
# print('Ejercicio 1: ', cuanto_tiempo()) # Ejercicio 1

# Ejercicio 2
def cadena_geringosa_for(palabra: str):
    palabra_nueva = ''
    
    for l in palabra:
        if l == 'a':
            palabra_nueva += 'apa'
        elif l == 'e':
            palabra_nueva += 'apa'
        elif l == 'i':
            palabra_nueva += 'apa'
        elif l == 'o':
            palabra_nueva += 'apa'
        elif l == 'u':
            palabra_nueva += 'apa'
        else:
            palabra_nueva += l

    return palabra_nueva

def cadena_geringosa_while(palabra: str):
    palabra_nueva = ''
    i = 0        
    while len(palabra) > i:
        if palabra[i] == 'a':
            palabra_nueva += 'apa'
        elif palabra[i] == 'e':
            palabra_nueva += 'apa'
        elif palabra[i] == 'i':
            palabra_nueva += 'apa'
        elif palabra[i]== 'o':
            palabra_nueva += 'apa'
        elif palabra[i] == 'u':
            palabra_nueva += 'apa'
        else:
            palabra_nueva += palabra[i]
        i += 1

    return palabra_nueva

# print('Ejercicio 2 con for: ', cadena_geringosa_for('geringosa')) # Ejercicio 2
# print('Ejercicio 2 con while: ', cadena_geringosa_while('geringosa')) # Ejercicio 2

# Ejercicio 3
def pertenece(lista: list, elem):
    for item in lista:
        if item == elem:
            return True
    return False

lista1 = [1,2,3,4,5,6,7,8,9]
# print('Ejercicio 3: ', pertenece(lista1, 10)) # Ejercicio 3
# print('Ejercicio 3: ', pertenece(lista1, 7)) # Ejercicio 3

# Ejercicio 4
def mas_Larga(lista1: list, lista2: list):
    if len(lista1) > len(lista2):
        return lista1
    return lista2


lista2 = [1,2,3,4,5]
lista3 = [1,2,3,4,5,6]
# print('Ejercicio 4: ', mas_Larga(lista1, lista2)) # Ejercicio 4
# print('Ejercicio 4: ', mas_Larga(lista1, lista3)) # Ejercicio 4
# print('Ejercicio 4: ', mas_Larga(lista3, lista2)) # Ejercicio 4

# Ejercicio 5
def rebotes():
    tabla = [[], []]
    i = 0
    h = 100
    factor = 3/5
    while i < 10:
        i += 1
        h = h * factor
        tabla[0].append('Salto ' + str(i))
        tabla[1].append(format_number(h))

    return tabla

# print('Ejercicio 5: ', rebotes()) # Ejercicio 5

# Ejercicio 6
def mezclar(cadena1, cadena2):
    res = ''
    letra_cadena_1 = 0
    long_cadena_1 = len(cadena1)
    long_cadena_2 = len(cadena2)
    
    if long_cadena_1 > long_cadena_2:
        cadena2 += ' ' * (long_cadena_1 - long_cadena_2)
    
    if long_cadena_1 < long_cadena_2:
        cadena1 += ' ' * (long_cadena_2 - long_cadena_1)

    for i in cadena1:
        res += i + cadena2[letra_cadena_1]
        letra_cadena_1 += 1
    
    res_sin_espacios = ''
    
    for i in res:
        if i != ' ':
            res_sin_espacios += i
    return res_sin_espacios


cadena1 = 'papá'
cadena2 = 'maslarga'
# print('Ejercicio 6: ', mezclar(cadena1, cadena2)) # Ejercicio 6
        
# Ejercicio 7
def intereses(monto, r, p = 12):
    return monto * r / p

def pago_capital(cuota, monto, r):
    return cuota - intereses(monto, r)

def monto_total():
    t = 30
    r = 0.05
    deuda = 500000
    cuota = 2684.11
    monto_total = cuota * t * 12

    # Parte a
    print('Monto total a pagar: ' + str(format_number(monto_total)))
    
    # Parte b
    cuota_extra = cuota + 1000
    capital_acumulado = 0
    intereses_acumulados = 0
    capital = 0
    meses = 0
    
    # 1er año
    while meses < 12:
        capital = pago_capital(cuota_extra, deuda, r)
        capital_acumulado += capital
        intereses_acumulados += cuota_extra - capital
        deuda -= capital
        meses += 1
    
    # luego del 1er año
    while deuda > 0:
        capital = pago_capital(cuota, deuda, r)
        capital_acumulado += capital
        intereses_acumulados += cuota - capital
        deuda -= capital
        meses += 1

    # ERROR en resultado de la guía, la última cuota excede la deuda por lo que se debe restar ese excedente
    monto_total_sin_excedente = format_number(capital_acumulado + deuda + intereses_acumulados)
    print('monto_total sin excedente de deuda:', monto_total_sin_excedente)
    
    monto_total_con_excedente = format_number(capital_acumulado + intereses_acumulados)
    print('monto_total con excedente de deuda:', monto_total_con_excedente)
    print('meses:', meses )

monto_total()

# Parte c
def calculo_financiero(monto, cuota, r, c):
    detalle = []
    intereses = monto * (r / (c * 100))
    capital = cuota - intereses
    detalle.append(format_number(cuota))
    detalle.append(format_number(capital))
    detalle.append(format_number(intereses))
    
    return detalle

    
def monto_total_params(pago_extra_monto, pago_extra_mes_comienzo, pago_extra_mes_fin):
    deuda = 500000
    cuota = 2684.11


    capital_acumulados = 0
    intereses_acumulados = 0
    i = 1
    
    # Periodo desde 0 hasta pago_extra_mes_comienzo
    while i < pago_extra_mes_comienzo:
        capital_acumulados += calculo_financiero(deuda, cuota, 5, 12)[1]
        intereses_acumulados += calculo_financiero(deuda, cuota, 5, 12)[2]
        i += 1
        
    deuda -= capital_acumulados
    
    # Periodo desde pago_extra_mes_comienzo hasta pago_extra_mes_fin
    while i < pago_extra_mes_fin:
        capital_acumulados += calculo_financiero(deuda, cuota + pago_extra_monto, 5, 12)[1]
        intereses_acumulados += calculo_financiero(deuda, cuota + pago_extra_monto, 5, 12)[2]
        i += 1
        
    deuda -= capital_acumulados
    
    # Periodo desde pago_extra_mes_fin hasta deuda = 0
    cuota_extra = cuota + pago_extra_monto
    while deuda > 0:
        capital = calculo_financiero(deuda, cuota_extra, 5, 12)[1]
        capital_acumulados += capital
        intereses_acumulados += calculo_financiero(deuda, cuota_extra, 5, 12)[2]
        i += 1
        deuda -= capital
    
    monto_total_pagado = capital_acumulados + intereses_acumulados + deuda

    return format_number(monto_total_pagado)
        

print('Ejercicio 7c: ', monto_total_params(1000, 61, 72))

# Ejercicio 8
def traductor_geringoso(lista):
    dictionary = {}
    for i in lista:
        dictionary[i] = cadena_geringosa_for(i)
    return dictionary
        
lista = ['banana', 'manzana', 'mandarina']
print(traductor_geringoso(lista))
