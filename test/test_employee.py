from src.models.employee import Employee

def test_employee_full_name():
    employee = Employee(
        employee_id=1,
        first_name="Juan",
        middle_initial="P",
        last_name="Lopez",
        birth_date="1980-01-01",
        gender="M",
        city_id=5,
        hire_date="2010-01-01"
    )
    assert employee.full_name() == "Juan P. Lopez"
