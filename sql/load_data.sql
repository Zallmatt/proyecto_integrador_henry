-- Activar local_infile (si tenés permisos)
SET GLOBAL local_infile = 1;

-- Guardar configuración original y setear SQL_MODE compatible
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION';

-- Crear y seleccionar base de datos
CREATE DATABASE IF NOT EXISTS grocery_sales;
USE grocery_sales;

-- Tabla: countries
CREATE TABLE IF NOT EXISTS countries (
    country_id INT PRIMARY KEY,
    country_name VARCHAR(100),
    country_code VARCHAR(5)
);

-- Tabla: cities
CREATE TABLE IF NOT EXISTS cities (
    city_id INT PRIMARY KEY,
    city_name VARCHAR(100),
    zip_code VARCHAR(10),
    country_id INT,
    FOREIGN KEY (country_id) REFERENCES countries(country_id)
);

-- Tabla: categories
CREATE TABLE IF NOT EXISTS categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100)
);

-- Tabla: products
CREATE TABLE IF NOT EXISTS products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(150),
    price DECIMAL(10,4),
    category_id INT,
    class VARCHAR(50),
    modify_time VARCHAR(10),
    resistant VARCHAR(50),
    is_allergic VARCHAR(10),
    vitality_days INT,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- Tabla: customers
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    middle_initial VARCHAR(10),
    last_name VARCHAR(100),
    city_id INT,
    address VARCHAR(255),
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
);

-- Tabla: employees
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    middle_initial VARCHAR(10),
    last_name VARCHAR(100),
    birth_date DATETIME,
    gender VARCHAR(10),
    city_id INT,
    hire_date DATETIME,
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
);

-- Tabla: sales
CREATE TABLE IF NOT EXISTS sales (
    sale_id INT PRIMARY KEY,
    employee_id INT,
    customer_id INT,
    product_id INT,
    quantity INT,
    discount DECIMAL(4,2),
    total_price DECIMAL(10,2),
    sale_time VARCHAR(10),
    transaction_number VARCHAR(30),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Carga de datos
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/countries.csv'
INTO TABLE countries
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/cities.csv'
INTO TABLE cities
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/categories.csv'
INTO TABLE categories
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/products.csv'
INTO TABLE products
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/customers.csv'
INTO TABLE customers
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/employees.csv'
INTO TABLE employees
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/sales.csv'
INTO TABLE sales
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Restaurar modo SQL original
SET SQL_MODE=@OLD_SQL_MODE;
