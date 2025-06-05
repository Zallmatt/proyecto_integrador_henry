
# 🛠 Proyecto Integrador - Sistema de Análisis de Ventas

Este proyecto simula el trabajo de un ingeniero de datos junior que se une a una startup para desarrollar un sistema robusto de análisis de ventas a partir de archivos CSV y una base de datos relacional.

---

## ✅ ¿Qué se hizo?

- Se creó un entorno virtual y archivo `requirements.txt`.
- Se diseñó una estructura profesional de carpetas (`src/`, `data/`, `sql/`, `tests/`, `docs/`).
- Se creó la base de datos y tablas con `load_data.sql`.
- Se cargaron archivos `.csv` a MySQL utilizando `LOAD DATA INFILE`.
- Se modelaron todas las entidades del sistema usando **POO en Python**, aplicando:
  - Encapsulamiento
  - Constructores
  - Métodos relevantes para el negocio
- Se implementaron **patrones de diseño**:
  - `Singleton` → para la clase de conexión a la base
  - `Factory Method` → para instanciar modelos desde datos tabulares
- Se agregó un método que permite ejecutar consultas SQL y devuelve los resultados como `pandas.DataFrame`.
- Se escribieron **pruebas unitarias con `pytest`** para verificar comportamiento de patrones y entidades.
- Se integró todo en un **Jupyter Notebook** de verificación llamado `verificacion_step_dos.ipynb`.

---

## 🗂 Estructura del proyecto

```
proyecto_integrador_henry/
│
├── data/                         # Archivos CSV
├── docs/                         # Documentación adicional
├── sql/                          # Script SQL para creación y carga de tablas
├── src/
│   ├── database/                 # Conector Singleton con SQLAlchemy
│   ├── factories/                # Factory Method
│   └── models/                   # Clases Python por entidad (POO)
├── test/                         # Pruebas unitarias con pytest
├── verificacion_step_dos.ipynb   # Notebook de validación final
├── requirements.txt              # Dependencias del entorno
├── .gitignore
└── .env                          # Variables sensibles (no versionadas)
```

---

## 📊 Validación final (`verificacion_step_dos.ipynb`)

El notebook de integración muestra:

- ✅ Conexión exitosa a la base
- 📈 Consulta SQL con salida como `DataFrame`
- 🏗 Instanciación de entidad usando patrón Factory
- 🔎 Ejecución de tests con `pytest` mostrando salida en notebook
- 📅 Mensaje final con timestamp de ejecución

---

## 🧠 Justificación técnica

- Se diseñó el sistema con enfoque modular y profesional.
- Se aplicaron buenas prácticas de arquitectura y patrones de diseño.
- Se automatizó la validación del sistema mediante notebook ejecutable y pruebas unitarias.
- Se garantizó la seguridad de las credenciales con `.env` y `.gitignore`.

---

## 🚀 Cómo ejecutar

1. Clonar el repositorio y navegar al proyecto.
2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # o venv\Scripts\activate en Windows
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Cargar los datos desde `sql/load_data.sql` usando MySQL Workbench.
5. Ejecutar el notebook `verificacion_step_dos.ipynb` o lanzar pruebas con:
   ```bash
   pytest
   ```

---

## 📬 Autor

Proyecto desarrollado en el marco del bootcamp Henry | Data Engineering.
