# 📊 Laboratorio de Datos - FCEn UBA

Repositorio del curso **Laboratorio de Datos** de la Facultad de Ciencias Exactas y Naturales (FCEn) - Universidad de Buenos Aires (UBA).

Este proyecto contiene material completo para un curso integral de ciencia de datos que cubre desde fundamentos de programación hasta técnicas avanzadas de machine learning.

## 🎯 Descripción del Curso

El curso está diseñado para proporcionar una formación completa en ciencia de datos, cubriendo todo el pipeline desde la adquisición de datos hasta el modelado predictivo. Se enfoca en aplicaciones prácticas usando Python y herramientas estándar de la industria.

## 📚 Contenido del Curso

### **Módulo 1: Fundamentos**

- **Clase 00**: Presentación de la Materia
- **Clase 01**: Python y Pandas - Manipulación y análisis de datos
- **Clase 02**: Introducción a la Metodología de análisis de datos

### **Módulo 2: Bases de Datos y SQL**

- **Clase 03**: Modelado de Datos - Diagramas Entidad-Relación (DER)
- **Clase 04**: Modelo Relacional
- **Clases 05-07**: Álgebra Relacional y SQL
- **Clases 08-09**: Normalización de bases de datos

### **Módulo 3: Análisis y Visualización**

- **Clase 10**: Calidad de Datos
- **Clases 11-12**: Visualización y Análisis Exploratorio de Datos (AED)

### **Módulo 4: Machine Learning**

- **Clase 13**: Introducción al Modelado
- **Clases 14-15**: Clasificación (Árboles de Decisión, KNN, Random Forest)
- **Clase 16**: Regresión Lineal Simple (RLS)
- **Clase 17**: Regresión KNN
- **Clase 18**: Selección de Modelos y Validación Cruzada
- **Clase 19**: Aprendizaje No Supervisado (Clustering)
- **Clases 20-21**: Temas avanzados

## 🛠️ Tecnologías Utilizadas

- **Python 3.x** - Lenguaje principal
- **Pandas** - Manipulación y análisis de datos
- **NumPy** - Computación numérica
- **Matplotlib/Seaborn** - Visualización de datos
- **Scikit-learn** - Machine Learning
- **DuckDB** - Consultas SQL en Python
- **SQL** - Gestión de bases de datos relacionales

## 📁 Estructura del Proyecto

```text
clases/
├── Clase-00-PresentacionMateria/
├── Clase-01-PythonPandas/           # Fundamentos de Python y Pandas
├── Clase-02-introMetodología/       # Metodología de análisis
├── Clase-03-ModeladoDeDatos-DER/    # Diagramas Entidad-Relación
├── Clase-04-ModeloRelacional/       # Bases de datos relacionales
├── Clase-05-06-07-AlgebraRelacional-SQL/  # SQL y álgebra relacional
├── Clase-08--09-Normalizacion/      # Normalización de BD
├── Clase-10-CalidadDeDatos/         # Calidad y limpieza de datos
├── Clase-11-12-Visualizacion AED/   # Análisis exploratorio
├── Clase-13-IntroModelado/          # Introducción al ML
├── Clase-14-15-Clasificacion/       # Algoritmos de clasificación
├── Clase-16-RLS/                    # Regresión lineal
├── Clase-17-RegresiónKNN/          # Regresión KNN
├── Clase-18-SeleccionModelos/       # Selección y validación
├── Clase-19-NoSupervisado/          # Clustering
├── clase-20/ & clase-21/            # Temas avanzados
└── evaluaciones/                    # Trabajos prácticos y parciales
```

## 📊 Datasets Incluidos

El curso utiliza diversos datasets reales para ejercicios prácticos:

- **Arbolado urbano** - Análisis de espacios verdes en Buenos Aires
- **Wine Quality** - Clasificación de calidad de vinos
- **Iris** - Conjunto de datos clásico para clasificación
- **Titanic** - Predicción de supervivencia
- **Tips** - Análisis de propinas en restaurantes
- **Datos epidemiológicos** - Casos de dengue y zika
- **Movilidad urbana** - Encuestas de transporte
- **MNIST modificado** - Reconocimiento de dígitos con ruido

> **Nota**: Los datasets grandes (>50MB) como `mnist_c_fog_tp.csv` y PDFs de bibliografía están excluidos del repositorio. Contactar al autor para obtener estos archivos si son necesarios para reproducir los experimentos.

## 🎓 Evaluaciones

### **Trabajo Práctico 1 (TP1)**

- **Tema**: Diseño de bases de datos relacionales
- **Contenido**: Modelado DER, normalización, implementación SQL
- **Archivos**: `evaluaciones/tp1/`

### **Trabajo Práctico 2 (TP2)**

- **Tema**: Clasificación y selección de modelos
- **Dataset**: MNIST con ruido (fog)
- **Técnicas**: KNN, Random Forest, Árboles de Decisión
- **Metodología**: Validación cruzada, análisis de métricas
- **Archivos**: `evaluaciones/tp2/`

## 🚀 Configuración del Entorno

### **Instalación Automática (Recomendado)**

```bash
# 1. Clonar el repositorio
git clone https://github.com/alexballera/laboratorio-fcen.git
cd laboratorio-fcen

# 2. Crear y activar entorno virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# 3. Instalar todas las dependencias
pip install -r requirements.txt

# 4. Verificar instalación
python test_environment.py
```

### **Instalación Manual**

```bash
# Instalar dependencias principales individualmente
pip install pandas numpy matplotlib seaborn scikit-learn duckdb jupyter
```

### **Verificación del Entorno**

```bash
# Verificación rápida
python -c "import pandas, numpy, sklearn, matplotlib, seaborn, duckdb; print('✅ Entorno OK')"
```

> 📋 **Ver documentación completa**: [ENVIRONMENT_SETUP.md](ENVIRONMENT_SETUP.md)

## 🗂️ Navegación Recomendada

1. **Comenzar con**: `Clase-01-PythonPandas/` para fundamentos
2. **Continuar con**: Las clases en orden numérico
3. **Practicar con**: Los datasets en cada directorio de práctica
4. **Evaluar con**: Los trabajos prácticos en `evaluaciones/`

### **Ejecutar Ejemplos**

```bash
# Activar entorno virtual (si no está activado)
source .venv/bin/activate

# Navegar a una clase específica
cd clases/Clase-01-PythonPandas/practica01/

# Ejecutar scripts de ejemplo
python ejercicios_clase1.py
python pandas_script1.py
```

### **Trabajar con Jupyter Notebooks**

```bash
# Activar entorno e iniciar Jupyter
source .venv/bin/activate
jupyter notebook
```

## 📁 Archivos de Configuración

- `requirements.txt` - Dependencias del proyecto
- `test_environment.py` - Script de verificación del entorno
- `ENVIRONMENT_SETUP.md` - Documentación detallada del entorno
- `.gitignore` - Archivos excluidos del repositorio

## 📈 Características Destacadas

- **📖 Progresión pedagógica clara**: Desde conceptos básicos hasta técnicas avanzadas
- **🔬 Enfoque práctico**: Ejercicios con datos reales
- **🛠️ Herramientas estándar**: Tecnologías usadas en la industria
- **📊 Análisis completo**: Desde limpieza hasta modelado
- **🎯 Aplicaciones reales**: Casos de uso del mundo real
- **📝 Documentación detallada**: Comentarios y explicaciones en el código

## 🤝 Contribuciones

Este es un proyecto educativo. Las contribuciones son bienvenidas para:

- Mejorar documentación
- Agregar ejemplos adicionales
- Corregir errores
- Actualizar dependencias

## 📄 Licencia

MIT License - ver archivo `LICENSE` para más detalles.

## 👨‍🎓 Autor

**Alexander Ballera** - Estudiante de Ciencias de Datos, FCEn UBA

---

*Este repositorio representa el trabajo realizado durante el curso de Laboratorio de Datos en la FCEn UBA, mostrando la evolución del aprendizaje desde conceptos básicos hasta implementaciones avanzadas de machine learning.*
