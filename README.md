# 📊 Laboratorio de Datos - FCEn UBA

Repositorio del curso **Laboratorio de Datos** (FCEn UBA). Contiene notebooks, scripts y datasets para prácticas y evaluaciones del curso.

## Estado y objetivo
Este repositorio es material docente: ejemplos, ejercicios prácticos y trabajos. Está optimizado para uso en clases y laboratorios; las instrucciones aquí permiten configurar el entorno local y ejecutar los materiales.

## Quickstart (rápido)
1. Clonar el repositorio:

```bash
git clone https://github.com/alexballera/laboratorio-fcen.git
cd laboratorio-fcen
```

2. Crear y activar entorno virtual (recomendado):

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / macOS
# .venv\Scripts\activate   # Windows
```

3. Instalar dependencias:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Verificar instalación mínima:

```bash
python test_environment.py
```

## Estructura principal

`clases/` contiene los materiales organizados por sesión. Cada subdirectorio tiene ejemplos y prácticas:

- `Clase-01-PythonPandas/`: Fundamentos de Python y Pandas
- `Clase-03-ModeladoDeDatos-DER/`: Modelado entidad-relación
- `evaluaciones/`: Trabajos prácticos y sus entregas

Explora `clases/` para encontrar notebooks y scripts asociados a cada clase.

## Notebooks y ejecución reproducible
- Preferir ejecutar notebooks desde el entorno virtual (`.venv`) para garantizar dependencias correctas.
- Antes de abrir notebooks en un entorno gestionado, ejecutar `configure_python_environment` y `configure_notebook` si están disponibles en tu plataforma para apuntar el kernel al `.venv`.

## Ejecutar ejemplos y scripts
Ejemplo para ejecutar un script de la clase 1:

```bash
source .venv/bin/activate
python clases/Clase-01-PythonPandas/practica/pandas_script1.py
```

## Tests y verificación
- `test_environment.py` comprueba que las dependencias principales están instaladas. Ejecutarlo tras instalar dependencias.
- Si se añaden tests adicionales, usar `pytest -q` (instalar `pytest` si es necesario).

## Contribuciones
Este repositorio admite contribuciones orientadas a mejorar la docencia:

- Corregir o mejorar notebooks y scripts
- Añadir ejercicios y datasets (evitar subir datos sensibles)
- Actualizar `requirements.txt` cuando agregues dependencias

Antes de enviar un PR:

1. Ejecutar `python test_environment.py` y/o `pytest -q`.
2. Verificar que los notebooks relevantes se ejecutan en orden.
3. Añadir notas en el PR sobre cambios en dependencias o datos.

## Recursos
- `ENVIRONMENT_SETUP.md`: instrucciones extendidas de instalación y compatibilidad.
- `requirements.txt`: lista de paquetes necesarios.

## Licencia y autor
- Licencia: MIT (ver `LICENSE`)
- Autor: Alexander Ballera

---

Si quieres, puedo:

- Generar una checklist automatizada para ejecutar antes de un PR.
- Crear un script `make setup` o `scripts/setup.sh` que automatice el Quickstart.
