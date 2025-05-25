from src.services.data_loader import (
    load_products,
    load_customers,
    load_employees,
    load_sales,
    load_cities,
    load_countries,
    load_categories
)

from src.services.insert_service import (
    insert_products,
    insert_customers,
    insert_employees,
    insert_sales,
    insert_cities,
    insert_countries,
    insert_categories
)

def mostrar_lista(nombre, lista, cantidad=3):
    print(f"\n🔹 {nombre} ({len(lista)} registros):")
    for item in lista[:cantidad]:
        print(f"   - {item}")

def main():
    print("📥 Cargando datos desde archivos CSV...")
    productos = load_products()
    clientes = load_customers()
    empleados = load_employees()
    ventas = load_sales()
    ciudades = load_cities()
    paises = load_countries()
    categorias = load_categories()

    mostrar_lista("Productos", productos)
    mostrar_lista("Clientes", clientes)
    mostrar_lista("Empleados", empleados)
    mostrar_lista("Ventas", ventas)
    mostrar_lista("Ciudades", ciudades)
    mostrar_lista("Países", paises)
    mostrar_lista("Categorías", categorias)

    print("\n🗄️ Insertando datos en MySQL...")
    insert_countries(paises)
    insert_cities(ciudades)
    insert_categories(categorias)
    insert_products(productos)
    insert_customers(clientes)
    insert_employees(empleados)
    insert_sales(ventas)
    print("\n✅ Inserción completada con éxito.")

if __name__ == "__main__":
    main()
