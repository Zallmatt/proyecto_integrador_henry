# Proyecto Integrador - Sistema de Análisis de Ventas

Este proyecto simula el trabajo de un ingeniero de datos junior en una empresa de retail. El objetivo es construir una solución completa de análisis de ventas, desde el modelado de datos hasta consultas avanzadas en SQL, integrando todo con Python de forma profesional y segura.

---

## ¿Qué se hizo?

### Etapa 1: Fundaciones del sistema

- Se creó un entorno virtual y se registraron las dependencias en `requirements.txt`.
- Se diseñó una estructura profesional de carpetas (`src/`, `data/`, `sql/`, `tests/`, etc.).
- Se creó la base de datos `grocery_sales` con sus tablas correspondientes en MySQL.
- Se cargaron datos reales desde archivos `.csv` usando `LOAD DATA INFILE`.
- Se implementó una arquitectura orientada a objetos:
- Cada tabla tiene su clase Python con encapsulamiento, constructor y métodos personalizados.
- Se crearon tests unitarios con `pytest`.

### Etapa 2: Conexión y diseño con patrones

- Se implementó el patrón Singleton en `DatabaseConnector` para garantizar una única conexión a la base de datos.
- Se implementó el patrón Factory para construir instancias de entidades desde estructuras externas (como filas de CSV).
- Se agregó un método para ejecutar consultas SQL desde Python y devolver los resultados como `pandas.DataFrame`.
- Se integraron pruebas y validaciones dentro de un **notebook ejecutable**.

### Etapa 3: Consultas avanzadas y automatización SQL

- Se crearon **consultas SQL avanzadas** usando:
  - CTE (Common Table Expressions)
  - Funciones ventana como `RANK()` y `ROW_NUMBER()`
- Se construyeron **objetos SQL**:
  - Vista enriquecida de ventas (`vista_ventas_enriquecidas`)
  - Procedimiento almacenado (`insertar_venta_simulada`) para insertar ventas desde Python
- Todo el sistema se ejecuta y documenta en un único Jupyter Notebook.

---

## Estructura del proyecto

```
proyecto_integrador_henry/
│
├── data/                      # Archivos CSV de entrada
├── docs/                      # Documentación técnica (.txt)
├── sql/                       # Script SQL para creación de tablas y objetos
├── src/
│   ├── database/              # Conexión a MySQL (Singleton)
│   ├── factories/             # Lógica Factory para entidades
│   └── models/                # Clases Python (POO)
├── test/                      # Tests con Pytest
├── venv/                      # Entorno virtual (ignorado)
├── .env                       # Credenciales (no versionado)
├── .gitignore
├── requirements.txt
├── proyecto_integrador_henry.ipynb   # Notebook con todas las integraciones
└── README.md
```

---

## Justificación técnica

- **Patrón Singleton**: evita múltiples conexiones innecesarias a la base.
- **Patrón Factory**: desacopla el proceso de construcción de entidades.
- **Funciones SQL avanzadas**: facilitan reportes rankeados, ordenados o contextualizados.
- **Procedimiento almacenado**: automatiza inserciones y reduce errores manuales.
- **Vista SQL**: concentra datos enriquecidos y listos para análisis.

---

### Cobertura de código

Se utilizaron pruebas automáticas con `pytest` y `pytest-cov`. La cobertura total alcanzó un **85%**, cumpliendo con los criterios de calidad y documentación.

![Coverage Report](docs\image.png)


## Cómo ejecutar

1. Clonar el repositorio.
2. Crear entorno virtual:

```bash
python -m venv venv
source venv/bin/activate   # o venv\Scripts\activate en Windows
pip install -r requirements.txt
```

3. Cargar la base de datos con el script `sql/load_data.sql` desde MySQL Workbench.
4. Verificar el archivo `.env` con tus credenciales de conexión.
5. Ejecutar el notebook:

```bash
jupyter notebook analisis_ventas_completo.ipynb
```

6. Ejecutar tests:

```bash
pytest
```

---

## 📬 Autor

Desarrollado por Matias Zalazar, en el marco del bootcamp Henry | Data Engineering.