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
# %% Ejercicio 1
def leer_parque(path, parque):
    df = pd.read_csv(path)

    arboles_df = df[df['espacio_ve'] == parque]
    
    # 3 formas de crear una lista de diccionarios a partir de un DataFrame de pandas
    # 1. https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html
    lista1 = arboles_df.to_dict(orient='records')
    
    columnas = arboles_df.columns
    lista2 = []
    
    # 2. construir dict usando las columnas y los valores de la fila
    for _, row in arboles_df.iterrows():
        registro = {col: row[col] for col in columnas}
        lista2.append(registro)
    
    # 3. construir dict usando las columnas y los valores de la fila
    lista3 = []
    i = 0
    
    for _, row in arboles_df.iterrows():
        registro = {}
        for item in row:
            registro[columnas[i]] = item
            i += 1
        lista3.append(registro)
        i = 0
    
    return lista1, lista2, lista3, df

# %% Ejercicio 2
def especies(lista_arboles):
    """Extrae el conjunto de especies únicas de la lista de árboles.
    
    Usa set comprehension para crear un conjunto sin duplicados.
    El acceso directo arbol['nombre_com'] asume que la clave existe.
    """
    arboles = set()
    
    # Set comprehension: crea un conjunto eliminando duplicados automáticamente
    arboles = {arbol['nombre_com'] for arbol in lista_arboles}

    return arboles
# %% Ejercicio 3
def contar_ejemplares(lista_arboles):
    """Cuenta la cantidad de ejemplares por especie.
    
    Devuelve 3 versiones del mismo resultado usando diferentes métodos.
    Todos usan .get() para acceso seguro evitando KeyError.
    
    .get(clave, default): busca 'clave' en el dict, si no existe devuelve 'default'
    """
    # Método 1: Counter (más eficiente y pythónico)
    # arbol.get('nombre_com') devuelve None si la clave no existe (evita KeyError)
    nombres = [arbol['nombre_com'] for arbol in lista_arboles if arbol.get('nombre_com')]
    result = dict(Counter(nombres))  # Counter cuenta automáticamente las ocurrencias
    
    # Método 2: dict con .get() para valores por defecto
    conteo = {}
    for arbol in lista_arboles:
        nombre = arbol.get('nombre_com')  # Devuelve None si no existe la clave
        if nombre:
            # conteo.get(nombre, 0) devuelve 0 si 'nombre' no está en conteo todavía
            conteo[nombre] = conteo.get(nombre, 0) + 1
    
    # Método 3: defaultdict (inicializa automáticamente con int() = 0)
    conteo2 = defaultdict(int)  # defaultdict(int) crea valores 0 automáticamente
    for arbol in lista_arboles:
        nombre = arbol.get('nombre_com')  # Acceso seguro, devuelve None si no existe
        if nombre:
            conteo2[nombre] += 1  # No necesita .get() porque defaultdict crea la clave
    conteo2 = dict(conteo2)  # Convertir de defaultdict a dict normal
        
    return result, conteo, conteo2

# %% Ejercicio 4
# ============================================================================
# VERSIÓN ANTERIOR (comentada para comparación):
# ============================================================================
# def obtener_altura(lista_arboles, especie):
#     # ❌ PROBLEMA 1: float() sin validación - puede lanzar ValueError
#     # ❌ PROBLEMA 2: No filtra valores None, '', NaN
#     # ❌ PROBLEMA 3: Acceso directo arbol['altura_tot'] puede dar KeyError
#     alturas = [float(arbol['altura_tot']) for arbol in lista_arboles if arbol.get('nombre_com') == especie]
#     return alturas
#
# def promedio(lista_numeros):
#     # ❌ PROBLEMA: ZeroDivisionError si lista_numeros está vacía
#     return round(sum(lista_numeros) / len(lista_numeros), 2)
#
# def maximo(lista_numeros):
#     # ❌ PROBLEMA: ValueError si lista_numeros está vacía
#     return round(max(lista_numeros), 2)
# ============================================================================

# VERSIÓN OPTIMIZADA:
def obtener_altura(lista_arboles, especie):
    """Obtiene las alturas de todos los ejemplares de una especie.
    
    MEJORAS:
    - Usa .get() para acceso seguro (evita KeyError)
    - Valida que altura no sea None, vacío o inválido
    - Maneja excepciones en conversión a float (try/except)
    - Retorna lista vacía si no hay ejemplares (comportamiento predecible)
    
    CONCEPTO CLAVE: Validación defensiva - asumir que los datos pueden estar
    incompletos o mal formateados y manejar todos los casos edge.
    """
    alturas = []
    for arbol in lista_arboles:
        if arbol.get('nombre_com') == especie:
            altura = arbol.get('altura_tot')  # .get() retorna None si no existe
            # Validar que altura tenga un valor útil
            if altura and str(altura).strip():  # Filtra None, '', espacios
                try:
                    alturas.append(float(altura))
                except (ValueError, TypeError):  # Captura errores de conversión
                    # Ignora valores que no se puedan convertir a float
                    continue
    return alturas

def promedio(lista_numeros):
    """Calcula el promedio de una lista de números.
    
    MEJORA: Guard clause - verifica condición de error primero y retorna.
    Evita ZeroDivisionError y hace el código más legible.
    
    CONCEPTO: 'Fail fast' - detectar problemas temprano y retornar valor seguro.
    """
    if not lista_numeros:  # Guard clause - chequeo temprano
        return 0.0
    return round(sum(lista_numeros) / len(lista_numeros), 2)

def maximo(lista_numeros):
    """Retorna el valor máximo de una lista.
    
    MEJORA: Mismo patrón que promedio() - guard clause para robustez.
    """
    if not lista_numeros:
        return 0.0
    return round(max(lista_numeros), 2)

# VERSIÓN ANTERIOR (comentada):
# def promedios(path, parques, especie):
#     medida = ['max', 'prom']
#     maximos = []
#     promedios = []
#     medidas = []  # ❌ Listas intermedias innecesarias
#
#     for parque in parques:
#         lista_arboles = leer_parque(path, parque)[0]
#         alturas = obtener_altura(lista_arboles, especie)
#
#         maximos.append(maximo(alturas))
#         promedios.append(promedio(alturas))
#
#     medidas.append(maximos)  # ❌ Construcción manual de estructura
#     medidas.append(promedios)
#     
#     # ❌ np.array() innecesario - pandas puede crear DataFrame directamente desde dict
#     df = pd.DataFrame(np.array(medidas), columns=parques, index=medida)
#
#     return df

# VERSIÓN OPTIMIZADA:
def promedios(path, parques, especie):
    """Calcula métricas (max y promedio) de altura por parque para una especie.
    
    MEJORAS:
    - Usa diccionario en lugar de múltiples listas (más claro)
    - Crea DataFrame directamente desde dict (más eficiente)
    - Evita conversión innecesaria a np.array()
    
    CONCEPTO: Estructura de datos apropiada - dict es más semántico que lista
    para datos etiquetados. Pandas optimiza la creación desde dict.
    """
    # Dict es más semántico que listas múltiples
    metricas = {'max': [], 'prom': []}
    
    for parque in parques:
        lista_arboles = leer_parque(path, parque)[0]
        alturas = obtener_altura(lista_arboles, especie)
        
        metricas['max'].append(maximo(alturas))
        metricas['prom'].append(promedio(alturas))
    
    # DataFrame.from_dict es más directo y eficiente que np.array()
    df = pd.DataFrame(metricas, index=parques).T
    return df

# %% Ejercicio 5
# ============================================================================
# VERSIÓN ANTERIOR:
# ============================================================================
# def obtener_inclinaciones(lista_arboles, especie):
#     # ❌ PROBLEMA 1: arbol['inclinacio'] acceso directo - puede dar KeyError
#     # ❌ PROBLEMA 2: No valida que inclinación sea numérica
#     # ❌ PROBLEMA 3: No filtra None o valores inválidos
#     inclinaciones = [arbol['inclinacio'] for arbol in lista_arboles if arbol.get('nombre_com') == especie]
#     return inclinaciones
# ============================================================================

# VERSIÓN OPTIMIZADA:
def obtener_inclinaciones(lista_arboles, especie):
    """Obtiene las inclinaciones de todos los ejemplares de una especie.
    
    MEJORAS:
    - Usa .get() para acceso seguro a 'inclinacio'
    - Valida que inclinacion no sea None antes de convertir
    - Maneja excepciones en conversión a float
    - Filtra valores inválidos automáticamente
    
    CONCEPTO: Mismo patrón defensivo que obtener_altura() - consistencia
    en el código hace que sea más mantenible y predecible.
    """
    inclinaciones = []
    for arbol in lista_arboles:
        if arbol.get('nombre_com') == especie:
            inclinacion = arbol.get('inclinacio')  # Acceso seguro
            if inclinacion is not None:  # Validación explícita
                try:
                    inclinaciones.append(float(inclinacion))
                except (ValueError, TypeError):
                    continue  # Silenciosamente ignora valores inválidos
    return inclinaciones

# %% Ejercicio 6
# ============================================================================
# VERSIÓN ANTERIOR:
# ============================================================================
# def especimen_mas_inclinado(lista_arboles):
#     inclinacion = 0  # ❌ PROBLEMA 1: Si todas las inclinaciones son negativas, retorna 0
#     for arbol in lista_arboles:
#         # ❌ PROBLEMA 2: Acceso directo arbol['inclinacio'] - puede dar KeyError
#         if arbol['inclinacio'] >= inclinacion:
#             # ❌ PROBLEMA 3: Acceso directo arbol['nombre_com'] - puede dar KeyError
#             especie = arbol['nombre_com']
#             inclinacion = arbol['inclinacio']
#     # ❌ PROBLEMA 4: Variable 'especie' puede no estar definida si lista vacía - UnboundLocalError
#     return especie, inclinacion
# ============================================================================

# VERSIÓN OPTIMIZADA:
def especimen_mas_inclinado(lista_arboles):
    """Encuentra el espécimen con mayor inclinación individual.
    
    MEJORAS CLAVE:
    - Inicializa con float('-inf') en lugar de 0 (maneja valores negativos)
    - Usa .get() para todos los accesos a diccionario
    - Valida existencia de datos antes de procesar
    - Retorna valores por defecto claros si no hay datos
    
    CONCEPTO 1: float('-inf') es el valor más pequeño posible, garantiza que
    cualquier número real sea mayor. Técnica estándar para algoritmos de máximo.
    
    CONCEPTO 2: Retornar tupla consistente (siempre 2 valores) hace el código
    más predecible - el caller siempre sabe qué esperar.
    """
    if not lista_arboles:  # Guard clause - caso base
        return None, 0.0
    
    max_inclinacion = float('-inf')  # Inicialización correcta para búsqueda de máximo
    especie_max = None
    
    for arbol in lista_arboles:
        inclinacion = arbol.get('inclinacio')  # Acceso seguro
        nombre = arbol.get('nombre_com')       # Acceso seguro
        
        # Validar que ambos campos existan antes de procesar
        if inclinacion is not None and nombre:
            try:
                inclinacion = float(inclinacion)
                if inclinacion > max_inclinacion:  # Algoritmo de máximo estándar
                    max_inclinacion = inclinacion
                    especie_max = nombre
            except (ValueError, TypeError):
                continue  # Ignora valores que no se pueden convertir
    
    # Si no se encontró ningún árbol válido, retornar valores por defecto
    if especie_max is None:
        return None, 0.0
    
    return especie_max, round(max_inclinacion, 2)

# %% Ejercicio 7
# ============================================================================
# VERSIÓN ANTERIOR (INEFICIENTE - O(n²)):
# ============================================================================
# def especie_promedio_mas_inclinada(lista_arboles):
#     arboles = {}
#     especies = []  # ❌ Lista innecesaria - solo almacena un dict
#     
#     for arbol in lista_arboles:  # ❌ PROBLEMA CRÍTICO: Loop O(n)
#         # ❌ obtener_inclinaciones() recorre toda la lista OTRA VEZ = O(n)
#         # Resultado: O(n) * O(n) = O(n²) - EXTREMADAMENTE INEFICIENTE
#         # Para 690 árboles: ~476,100 operaciones en lugar de ~690
#         arboles[arbol.get('nombre_com')] = obtener_inclinaciones(lista_arboles, arbol.get('nombre_com'))
#     
#     especies.append(arboles)  # ❌ Wrapping innecesario en lista
#     
#     especies_prom = []  # ❌ Otra lista innecesaria
#     arboles = {}
#     
#     for k, v in especies[0].items():  # ❌ Acceso a especies[0] innecesario
#         arboles[k] = promedio(v)
#     especies_prom.append(arboles)  # ❌ Otro wrapping innecesario
#     
#     inclinacion = 0  # ❌ Mismo problema que ejercicio 6
#     for k, v in especies_prom[0].items():
#         if v >= inclinacion:
#             especie = k
#             inclinacion = v
#     # ❌ Variable 'especie' puede no estar definida
#     return especie, inclinacion
# ============================================================================

# VERSIÓN OPTIMIZADA (O(n)):
def especie_promedio_mas_inclinada(lista_arboles):
    """Encuentra la especie con mayor inclinación promedio.
    
    MEJORA CRÍTICA: Reduce complejidad de O(n²) a O(n) usando defaultdict.
    
    EXPLICACIÓN DE COMPLEJIDAD:
    - Versión anterior: para cada árbol (n), recorre toda la lista (n) → O(n²)
    - Versión optimizada: recorre la lista UNA VEZ, agrupa en memoria → O(n)
    - Ganancia: para 690 árboles, pasa de ~476,100 a ~690 operaciones (~690x más rápido)
    
    CONCEPTOS CLAVE:
    1. defaultdict(list): crea listas automáticamente, evita KeyError
    2. Una sola pasada: procesa cada elemento exactamente una vez
    3. Agrupación en memoria: más eficiente que re-filtrar la lista
    4. Dict comprehension: sintaxis pythónica y eficiente para transformaciones
    5. max() con key: encuentra máximo sin loop manual
    
    PATRÓN: Agregar → Transformar → Reducir (paradigma funcional)
    """
    from collections import defaultdict
    
    if not lista_arboles:  # Guard clause
        return None, 0.0
    
    # PASO 1: Agrupar inclinaciones por especie (una sola pasada - O(n))
    # defaultdict(list) crea lista vacía automáticamente si la clave no existe
    inclinaciones_por_especie = defaultdict(list)
    
    for arbol in lista_arboles:
        nombre = arbol.get('nombre_com')
        inclinacion = arbol.get('inclinacio')
        
        if nombre and inclinacion is not None:
            try:
                # Agrupar directamente sin llamar a obtener_inclinaciones()
                inclinaciones_por_especie[nombre].append(float(inclinacion))
            except (ValueError, TypeError):
                continue
    
    if not inclinaciones_por_especie:
        return None, 0.0
    
    # PASO 2: Calcular promedios (dict comprehension - pythónico y eficiente)
    # Itera sobre items() una vez, crea nuevo dict con promedios
    promedios_especies = {
        especie: promedio(inclinaciones)
        for especie, inclinaciones in inclinaciones_por_especie.items()
    }
    
    # PASO 3: Encontrar el máximo (función built-in optimizada en C)
    # key=lambda x: x[1] indica que compare por el segundo elemento (promedio)
    # Retorna la tupla (especie, promedio) con mayor promedio
    especie_max, promedio_max = max(promedios_especies.items(), key=lambda x: x[1])
    
    return especie_max, promedio_max

# %%
# %% main
if __name__ == '__main__':
    especie = 'Jacarandá'
    path = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ministerio-de-espacio-publico-e-higiene-urbana/arbolado-espacios-verdes/arbolado-en-espacios-verdes.csv'
    path2 = '/home/alexballera/Documents/uba/laboratorio-fcen/clases/Clase-01-PythonPandas/practica/arbolado-en-espacios-verdes.csv'
    parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']

    # Ejercicio 1
    print('='*60)
    lista1, lista2, lista3, df = leer_parque(path2, parques[1])
    print(f"Ejercicio1: Árboles en {parques[0]}: {len(lista1)}\n")
    
    # Ejercicio 2
    print('='*60)
    arboles = especies(lista3)
    print(f"Ejercicio2: Especies en {parques[0]}: {len(arboles)}\n")
    
    # Ejercicio 3
    print('='*60)
    cantidad_especies = contar_ejemplares(lista1)
    # .get('Jacarandá', 0) busca la clave, si no existe devuelve 0 (evita KeyError)
    print(f"Ejercicio 3: Cant de {especie} = {cantidad_especies[0].get(especie, 0)}\n")
    
    # Ejercicio 4
    print('='*60)
    alturas = obtener_altura(lista2, especie)
    h_maximo = maximo(alturas)
    h_mean = promedio(alturas)
    print(f'Ejercicio 4: alturas de {especie}: {alturas} ')
    print(f'Ejercicio 4: máximo de {especie}: {h_maximo} ')
    print(f'Ejercicio 4: promedio de {especie}: {h_mean}\n ')
    
    proms = promedios(path2, parques, especie)
    print(f"""

Ejercicio 4:
Métricas {especie}:
              
    {proms} """)
    
    # Ejercicio 5
    print('='*60)
    inclinaciones = obtener_inclinaciones(lista1, especie)
    print(f'Ejercicio 5: inclinaciones de {especie}: {inclinaciones}\n')
    
    # Ejercicio 6
    print('='*60)
    especie, inclinacion = especimen_mas_inclinado(lista1)
    print(f'Ejercicio 6: Especie más inclinada: {especie}, inclinación: {inclinacion}\n')
    
    # Ejercicio 7
    print('='*60)
    especie, inclinacion = especie_promedio_mas_inclinada(lista1)
    print(f'Ejercicio 7: Especie más inclinada promedio: {especie}, inclinación: {inclinacion}\n')

# %%