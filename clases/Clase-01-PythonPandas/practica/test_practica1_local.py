from pathlib import Path
import csv
import importlib.util


def test_leer_parque_local(tmp_path):
    # escribir un CSV pequeño en tmp_path
    p = tmp_path / "sample_local.csv"
    rows = [
        {"espacio_ve": "GENERAL PAZ", "nombre_cie": "Palo borracho", "altura_tot": 10},
        {"espacio_ve": "OTRO PARQUE", "nombre_cie": "Eucalipto", "altura_tot": 8},
        {"espacio_ve": "GENERAL PAZ", "nombre_cie": "Plátano", "altura_tot": 6},
    ]
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    # Cargar el módulo practica1.py por ruta (está en la misma carpeta que este test)
    this_dir = Path(__file__).resolve().parent
    mod_path = this_dir / 'practica1.py'
    spec = importlib.util.spec_from_file_location('practica1', str(mod_path))
    practica = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(practica)

    # llamar a la función con el CSV temporal
    resultado = practica.leer_parque(str(p), 'GENERAL PAZ')
    assert isinstance(resultado, list)
    assert len(resultado) == 2
    assert resultado[0]['espacio_ve'] == 'GENERAL PAZ'
