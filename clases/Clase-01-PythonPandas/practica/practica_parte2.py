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
import pandas as pd
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

# %% Ejercicio 9
# ============================================================================
# VERSIÓN ANTERIOR (CÓDIGO PROBLEMÁTICO):
# ============================================================================
# def add_column_ambiente(df_parque, df_vereda):
#     # ❌ PROBLEMA 1: Sintaxis incorrecta - doble corchete [['ambiente']] para asignar
#     #    Debería ser ['ambiente'] (sin lista) para asignar a una columna
#     #    El doble corchete se usa para SELECCIONAR múltiples columnas, no para asignar
#     df_parque[['ambiente']] = 'parque'
#     df_vereda[['ambiente']] = 'vereda'
#     
#     # ❌ PROBLEMA 2: Modifica los DataFrames originales (mutación in-place)
#     #    Si los DataFrames se usan después, tienen efectos secundarios no deseados
#     #    Viola el principio de funciones puras
#     
#     return df_parque, df_vereda
# ============================================================================

# VERSIÓN OPTIMIZADA:
def add_column_ambiente(df_parque, df_vereda):
    """Añade columna 'ambiente' a DataFrames de parque y vereda.
    
    MEJORAS CRÍTICAS:
    1. Usa .copy() para no modificar los DataFrames originales (inmutabilidad)
    2. Sintaxis correcta: ['ambiente'] en lugar de [['ambiente']]
    3. Usa .assign() como alternativa pythónica (método funcional)
    
    CONCEPTOS CLAVE:
    
    CONCEPTO 1: Inmutabilidad - funciones puras
    - ❌ Modificar parámetros in-place → efectos secundarios, difícil de debuggear
    - ✅ Retornar nuevos objetos → predecible, testeable, sin sorpresas
    
    CONCEPTO 2: Sintaxis de pandas para columnas
    - df[['col1', 'col2']]  → SELECCIONAR múltiples columnas (retorna DataFrame)
    - df['col']             → SELECCIONAR/ASIGNAR una columna (Series o asignación)
    - df[['col']] = valor   → INCORRECTO (funciona pero no es la forma idónea)
    - df['col'] = valor     → CORRECTO (asignación directa)
    
    CONCEPTO 3: .assign() - método funcional de pandas
    - Sintaxis: df.assign(nueva_col=valor)
    - Retorna NUEVO DataFrame sin modificar el original
    - Más pythónico y encadenable (method chaining)
    
    Args:
        df_parque: DataFrame con árboles de parques
        df_vereda: DataFrame con árboles de veredas
        
    Returns:
        tuple: (df_parque_con_ambiente, df_vereda_con_ambiente)
    """
    # OPCIÓN 1: Usar .copy() y asignación directa (más explícito)
    df_parque_nuevo = df_parque.copy()
    df_vereda_nuevo = df_vereda.copy()
    
    # Sintaxis correcta: ['ambiente'] sin doble corchete
    df_parque_nuevo['ambiente'] = 'parque'
    df_vereda_nuevo['ambiente'] = 'vereda'
    
    return df_parque_nuevo, df_vereda_nuevo
    
    # OPCIÓN 2: Usar .assign() - más funcional y pythónico
    # return (
    #     df_parque.assign(ambiente='parque'),
    #     df_vereda.assign(ambiente='vereda')
    # )
    # Ventaja: más conciso, inmutable por defecto, encadenable

# %% Ejercicio 10
# ============================================================================
# VERSIÓN ANTERIOR (BÁSICA):
# ============================================================================
# def concatenar(df_parque, df_vereda):
#     # ❌ PROBLEMA 1: No valida entrada (DataFrames vacíos o None)
#     # ❌ PROBLEMA 2: No maneja índices duplicados - puede causar problemas
#     # ❌ PROBLEMA 3: No especifica parámetros importantes de concat
#     #    - ignore_index: si no se especifica, mantiene índices originales (puede duplicar)
#     #    - axis: por defecto es 0 (filas), pero ser explícito es mejor
#     return pd.concat([df_parque, df_vereda])
# ============================================================================

# VERSIÓN OPTIMIZADA:
def concatenar(df_parque, df_vereda):
    """Concatena verticalmente DataFrames de parque y vereda.
    
    MEJORAS:
    1. Valida entrada - maneja DataFrames vacíos o None
    2. Usa ignore_index=True para resetear índices (evita duplicados)
    3. Especifica axis=0 explícitamente (mejor legibilidad)
    
    CONCEPTOS CLAVE:
    
    CONCEPTO 1: pd.concat() - unión de DataFrames
    - axis=0 (default) → concatena VERTICALMENTE (añade filas)
    - axis=1 → concatena HORIZONTALMENTE (añade columnas)
    - ignore_index=True → resetea índices (0, 1, 2, ..., n)
    - ignore_index=False (default) → mantiene índices originales (puede duplicar)
    
    CONCEPTO 2: Índices duplicados son problemáticos
    - Si df1 tiene índices [0,1,2] y df2 tiene [0,1,2]
    - concat sin ignore_index → resultado tiene [0,1,2,0,1,2] (duplicados)
    - .loc[0] retorna MÚTIPLES filas - comportamiento confuso
    - ignore_index=True → resultado tiene [0,1,2,3,4,5] (sin duplicados)
    
    CONCEPTO 3: Validación defensiva con listas
    - Filtrar DataFrames válidos antes de concat
    - Evita errores si alguno es None o vacío
    - Retorna DataFrame vacío con estructura correcta si no hay datos
    
    Args:
        df_parque: DataFrame con árboles de parques (con columna 'ambiente')
        df_vereda: DataFrame con árboles de veredas (con columna 'ambiente')
        
    Returns:
        DataFrame: Unión vertical de ambos DataFrames con índice reseteado
    """
    # Validación defensiva - construir lista de DataFrames válidos
    dfs_validos = []
    
    if df_parque is not None and not df_parque.empty:
        dfs_validos.append(df_parque)
    if df_vereda is not None and not df_vereda.empty:
        dfs_validos.append(df_vereda)
    
    # Si no hay DataFrames válidos, retornar DataFrame vacío con estructura
    if not dfs_validos:
        # Inferir columnas del primer DataFrame no vacío, o usar estructura básica
        columnas = ['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol', 'ambiente']
        return pd.DataFrame(columns=columnas)
    
    # Concatenar verticalmente (axis=0) reseteando índices
    # ignore_index=True → evita índices duplicados, crea secuencia 0,1,2,...,n
    return pd.concat(
        dfs_validos,
        axis=0,              # Concatenar verticalmente (añadir filas)
        ignore_index=True    # Resetear índices para evitar duplicados
    )
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
    
    # Ejercicio 9
    print('='*60)
    print('Ejercicio 9')
    df_tipas_parques, df_tipas_veredas = add_column_ambiente(df_tipas_parques, df_tipas_veredas)
    
    # Verificar resultados
    print(f"Columnas en parques: {df_tipas_parques.columns}")
    print(f"Columnas en veredas: {df_tipas_veredas.columns}")
    print("\nPrimeros 3 árboles en parques:")
    print(df_tipas_parques.head(3))
    print("\nPrimeros 3 árboles en veredas:")
    print(df_tipas_veredas.head(3))
    
    # Ejercicio 10
    print('='*60)
    print('Ejercicio 10')
    df_concatenado = concatenar(df_tipas_parques, df_tipas_veredas)
    
    # Verificar resultados
    print(f"Columnas en nuevo df: {df_concatenado.columns}")
    print("\nPrimeros 3 árboles:")
    print(df_concatenado.head(3))
    print("\nÚltimos 3 árboles:")
    print(df_concatenado.tail(3))
    
    

# %%