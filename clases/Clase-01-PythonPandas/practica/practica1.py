#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alex Ballera
"""
# %% Importo las librerías
from pathlib import Path
import pandas as pd

# %% Ejercicio 1
def leer_parque(nombre_archivo, parque):
    """Leer `nombre_archivo` y devolver una lista de registros (dict)
    con los árboles que pertenecen al `parque` indicado.

    `nombre_archivo` puede ser una ruta absoluta o un nombre relativo. Si
    no se encuentra como ruta absoluta, se buscará relativo al directorio
    donde está este script.
    """
    path = Path(nombre_archivo)
    if not path.is_file():
        path = Path(__file__).resolve().parent / nombre_archivo

    df = pd.read_csv(path)
    arboles_df = df[df['espacio_ve'] == parque]
    registros = arboles_df.to_dict(orient='records')
    return registros


def main():
    nombre_archivo = 'arbolado-en-espacios-verdes.csv'
    parque = 'GENERAL PAZ'
    registros = leer_parque(nombre_archivo, parque)
    print(f"Árboles en {parque}: {len(registros)}")


def ejecutar_ejercicio_1():
    """Función que actúa como la 'celda' del ejercicio 1.

    Se puede llamar desde la línea de comandos con `--ejercicio 1`
    o directamente desde un REPL/import.
    """
    nombre_archivo = 'arbolado-en-espacios-verdes.csv'
    parque = 'GENERAL PAZ'
    registros = leer_parque(nombre_archivo, parque)
    print(f"Árboles en {parque}: {len(registros)}")


def ejecutar_todos():
    ejecutar_ejercicio_1()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Ejercicios prácticos - Clase 01')
    parser.add_argument('-e', '--ejercicio', help='Número de ejercicio a ejecutar (ej: 1) o "all"', default=None)
    args = parser.parse_args()

    if args.ejercicio is None:
        # comportamiento por defecto: ejecutar main (demostración rápida)
        main()
    else:
        if args.ejercicio in ('1', '01'):
            ejecutar_ejercicio_1()
        elif args.ejercicio in ('all', 'todos'):
            ejecutar_todos()
        else:
            print(f"Ejercicio '{args.ejercicio}' no reconocido.")

# %%