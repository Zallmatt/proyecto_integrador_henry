# 🛒 Proyecto Integrador - Análisis de Ventas para Supermercados

## ✅ ¿Qué se hizo?

Este proyecto simula el trabajo de un ingeniero de datos junior en una empresa de supermercados. Se desarrolló un sistema completo para:

- Modelar entidades clave del negocio usando Programación Orientada a Objetos (POO)
- Cargar archivos `.csv` con datos reales
- Crear e insertar datos en una base de datos MySQL
- Aplicar principios de diseño profesional, como separación por capas y pruebas unitarias
- Realizar la carga desde Python usando `pandas` y `SQLAlchemy`
- Implementar pruebas unitarias con `pytest`

---

## 📁 Organización del proyecto

```
sales_analytics_project/
├── data/                 # Archivos .csv (productos, ventas, etc.)
├── sql/                  # Scripts SQL (creación y carga de tablas)
├── src/
│   ├── models/           # Clases POO (Product, Customer, etc.)
│   └── services/         # Carga de datos, conexión DB, inserción
├── tests/                # Pruebas unitarias con pytest
│
├── main.py               # Script principal de ejecución
├── .env                  # Credenciales de conexión MySQL
├── .gitignore            # Ignorar venv, __pycache__, .env
├── requirements.txt      # Dependencias
└── README.md             # Documentación del proyecto
```

---

## ⚙️ Justificación técnica

- **POO**: Se crearon clases por entidad del negocio para encapsular lógica como `is_perishable()` o `full_name()`.
- **Carga de datos**: Se usó `pandas` para leer `.csv` y transformar en objetos Python.
- **Base de datos relacional**: MySQL para almacenar los datos estructurados.
- **SQLAlchemy + PyMySQL**: Para facilitar la conexión e inserción sin escribir sentencias SQL manuales.
- **.env**: Uso de variables de entorno para ocultar credenciales.
- **pytest**: Se escribieron pruebas unitarias para asegurar la funcionalidad de clases clave.
- **Escalabilidad**: El sistema está modularizado y preparado para aplicar transformaciones, validaciones, ETLs o reporting.

---

## 🚀 Cómo ejecutar

1. Crear entorno virtual y activar:

```bash
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Configurar `.env`:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=tu_contraseña
DB_NAME=grocery_sales
```

4. Ejecutar el sistema:

```bash
python main.py
```

5. Ejecutar pruebas:

```bash
pytest
```