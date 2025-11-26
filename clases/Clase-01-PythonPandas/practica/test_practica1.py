from pathlib import Path
import csv
from importlib import util


def test_leer_parque_tmp(tmp_path):
    # Crear un CSV de prueba
    p = tmp_path / "sample.csv"
    rows = [
        {"espacio_ve": "GENERAL PAZ", "nombre_cie": "Palo borracho", "altura_tot": 10},
        {"espacio_ve": "OTRO PARQUE", "nombre_cie": "Eucalipto", "altura_tot": 8},
        {"espacio_ve": "GENERAL PAZ", "nombre_cie": "Plátano", "altura_tot": 6},
    ]
    # Escribir CSV (columnas en el orden deseado)
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    # Cargar el módulo practica1.py por ruta (está en la misma carpeta que este test)
    this_dir = Path(__file__).resolve().parent
    mod_path = this_dir / 'practica1.py'
    spec = util.spec_from_file_location('practica1', str(mod_path))
    practica = util.module_from_spec(spec)
    spec.loader.exec_module(practica)

    resultado = practica.leer_parque(str(p), "GENERAL PAZ")
    # Debe devolver sólo los 2 registros de GENERAL PAZ
    assert isinstance(resultado, list)
    assert len(resultado) == 2
    # comprobar que las claves existen
    assert "nombre_cie" in resultado[0]
    assert resultado[0]["espacio_ve"] == "GENERAL PAZ"
