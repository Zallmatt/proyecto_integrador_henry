
# 🛠 Proyecto Integrador - Sistema de Análisis de Ventas

Este proyecto simula el trabajo de un ingeniero de datos junior que se une a una startup para desarrollar un sistema robusto de análisis de ventas a partir de archivos CSV y una base de datos relacional.

---

## ✅ ¿Qué se hizo?

- Se creó un entorno virtual y archivo `requirements.txt`.
- Se diseñó una estructura profesional de carpetas (`src/`, `data/`, `sql/`, `tests/`).
- Se creó la base de datos y tablas con `load_data.sql`.
- Se cargaron archivos `.csv` a MySQL utilizando `LOAD DATA INFILE`.
- Se modelaron todas las entidades del sistema usando **POO en Python**, aplicando:
  - Encapsulamiento
  - Constructores
  - Métodos relevantes para el negocio
- Se implementó una **prueba unitaria con `pytest`** para validar funcionalidad.

---

## 🗂 Estructura del proyecto

```
proyecto_integrador/
│
├── data/               # Archivos CSV
├── sql/                # Script SQL para creación y carga de tablas
├── src/
│   └── models/         # Clases Python por entidad (POO)
├── tests/              # Pruebas unitarias (pytest)
├── requirements.txt    # Dependencias del entorno
├── README.md           # Documentación principal
├── .gitignore
└── .env                # Variables sensibles (no versionadas)
```

---

## 🧠 Justificación técnica

- Uso de **clases por entidad** directamente mapeadas a los CSV.
- Métodos como `precio_final()`, `nombre_completo()`, `total_con_descuento()` reflejan reglas del negocio.
- Estructura escalable que permite incorporar análisis avanzados, consultas SQL complejas, visualización de datos o dashboards.
- Uso de `pytest` para asegurar funcionamiento correcto de la lógica.

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
4. Cargar los datos desde `load_data.sql` usando MySQL Workbench.
5. Ejecutar los tests:
   ```bash
   pytest
   ```

---

## 📬 Autor

Proyecto desarrollado en el marco del bootcamp Henry | Data Engineering.
