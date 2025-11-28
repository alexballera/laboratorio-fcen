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
# ============================================================================
# VERSIÓN ANTERIOR:
# ============================================================================
# def preparacion_df(path):
#     arboles_veredas = pd.read_csv(path)
#     df = pd.DataFrame(arboles_veredas)  # ❌ REDUNDANTE: pd.read_csv ya retorna DataFrame
#     
#     data_arboles_veredas = df[['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho']]
#     return data_arboles_veredas, df
# ============================================================================

# VERSIÓN OPTIMIZADA:
def preparacion_df(path):
    """Carga datos de arbolado desde CSV y retorna subconjunto de columnas.
    
    MEJORA: Elimina conversión redundante pd.DataFrame() - read_csv() ya retorna DataFrame.
    
    CONCEPTO: No duplicar trabajo - read_csv retorna un DataFrame, no necesita conversión.
    Hacer esto es como convertir un int a int: innecesario y confuso.
    
    Args:
        path: Ruta al archivo CSV (local o URL)
        
    Returns:
        tuple: (data_arboles_veredas con 3 columnas, df completo)
    """
    # pd.read_csv ya retorna un DataFrame - no necesita conversión
    df = pd.read_csv(path)
    
    # Seleccionar columnas de interés
    data_arboles_veredas = df[['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho']]
    return data_arboles_veredas, df

# %% ejercicio 8
# ============================================================================
# VERSIÓN ANTERIOR (CÓDIGO PROBLEMÁTICO):
# ============================================================================
# def parques_veredas_df():
#     # ❌ PROBLEMA CRÍTICO 1: Usa variable global 'df' - función NO autónoma
#     #    Si 'df' no existe o cambia externamente, la función falla o da resultados incorrectos
#     arboles = df[['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol', 'ancho_acera']]
#     
#     # ❌ PROBLEMA 2: Compara string con string - 'ancho_acera' > '0'
#     #    Esto NO funciona correctamente porque:
#     #    - Si ancho_acera es numérico (float), falla con TypeError
#     #    - Si es string, compara alfabéticamente: '10' < '2' (incorrecto)
#     vereda = arboles[arboles['ancho_acera'] > '0']
#     
#     # ❌ PROBLEMA 3: Selecciona columnas DESPUÉS de filtrar
#     #    Ineficiente - carga datos que luego descarta
#     parque = arboles[arboles['ancho_acera'].isna()]
#     
#     vereda = vereda[['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol']]
#     parque = parque[['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol']]
#
#     return parque, vereda
# ============================================================================

# VERSIÓN OPTIMIZADA:
def parques_veredas_df(df):
    """Separa árboles en parques vs veredas según presencia de ancho_acera.
    
    MEJORAS CRÍTICAS:
    1. Recibe 'df' como parámetro - función pura, sin dependencias globales
    2. Compara numéricamente (> 0) en lugar de string (> '0')
    3. Usa .copy() para evitar SettingWithCopyWarning
    
    CONCEPTOS CLAVE:
    
    CONCEPTO 1: Variables globales son ANTIPATRÓN
    - ❌ Función que usa global 'df' → acoplamiento, difícil de testear
    - ✅ Función con parámetro 'df' → reutilizable, testeable, clara
    
    CONCEPTO 2: Comparación numérica vs string
    - ❌ '10' > '2' retorna False (compara alfabéticamente)
    - ✅  10 > 2 retorna True (compara numéricamente)
    - pd.to_numeric convierte strings a float, maneja errores con coerce
    
    CONCEPTO 3: .copy() evita SettingWithCopyWarning
    - Cuando haces df[condicion], pandas puede retornar vista o copia
    - Modificar vista puede afectar el DataFrame original sin querer
    - .copy() garantiza DataFrame independiente
    
    CONCEPTO 4: Separación lógica clara
    - Vereda: ancho_acera > 0 (tiene vereda medible)
    - Parque: ancho_acera es NaN (no tiene vereda, está en parque)
    
    Args:
        df: DataFrame con datos completos de arbolado
        
    Returns:
        tuple: (df_parque, df_vereda) ambos con columnas [nombre_cientifico, 
                diametro_altura_pecho, altura_arbol]
    """
    # Validación de entrada - defensive programming
    if df is None or df.empty:
        # CONCEPTO: Crear una sola estructura vacía y retornarla dos veces
        # así que es seguro retornar la misma referencia.
        # NOTA: Si necesitáramos modificar los DataFrames después, SÍ deberíamos
        # crear copias separadas con .copy()
        columnas = ['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol']
        df_vacio = pd.DataFrame(columns=columnas)
        return df_vacio, df_vacio  # Misma referencia - más eficiente en memoria
    
    # Convertir ancho_acera a numérico (maneja strings, NaN, etc.)
    # coerce=True convierte valores inválidos a NaN en lugar de lanzar error
    df_trabajo = df.copy()  # Trabajar con copia para no modificar original
    df_trabajo['ancho_acera_num'] = pd.to_numeric(df_trabajo['ancho_acera'], errors='coerce')
    
    # Seleccionar columnas de interés primero (más eficiente)
    columnas_finales = ['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol']
    
    # FILTRO VEREDAS: ancho_acera > 0 (tiene vereda medible)
    # Nota: .notna() asegura que no incluimos NaN
    mascara_vereda = (df_trabajo['ancho_acera_num'].notna()) & (df_trabajo['ancho_acera_num'] > 0)
    df_vereda = df_trabajo.loc[mascara_vereda, columnas_finales].copy()
    
    # FILTRO PARQUES: ancho_acera es NaN (sin vereda → en parque)
    mascara_parque = df_trabajo['ancho_acera_num'].isna()
    df_parque = df_trabajo.loc[mascara_parque, columnas_finales].copy()
    
    return df_parque, df_vereda
# %% main
if __name__ == '__main__':
    path1 = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/atencion-ciudadana/arbolado-publico-lineal/arbolado-publico-lineal-2017-2018.csv'
    path2 = '/home/alexballera/Documents/uba/laboratorio-fcen/clases/Clase-01-PythonPandas/practica/arbolado-publico-lineal-2017-2018.csv'
    especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
    
    # preparacion_df
    data_arboles_veredas, df = preparacion_df(path2)

    # Ejercicio 8
    print('='*60)
    # Pasar 'df' como parámetro - función pura sin dependencias globales
    df_tipas_parques, df_tipas_veredas = parques_veredas_df(df)
    
    # Verificar resultados
    print(f"Árboles en parques: {len(df_tipas_parques)}")
    print(f"Árboles en veredas: {len(df_tipas_veredas)}")
    print("\nPrimeros 3 árboles en parques:")
    print(df_tipas_parques.head(3))
    print("\nPrimeros 3 árboles en veredas:")
    print(df_tipas_veredas.head(3))

# %%