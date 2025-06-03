import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Busca en el directorio padre
from src.models.employee import Employee

def test_antiguedad():
    empleado = Employee(1, "Lucas", "A", "Pare", "1990-05-15", "M", 1, "2020-01-01")
    assert empleado.antiguedad() == "Empleado desde 2020"