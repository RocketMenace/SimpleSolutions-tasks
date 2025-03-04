import os
from services import get_data

from db_manager import DatabaseConnector, DatabaseManager
from dotenv import load_dotenv

load_dotenv()

db_params = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": os.getenv("DB_PORT"),
}

db_connector = DatabaseConnector(db_name="employees")
connection, cursor = db_connector.open_connection(db_params)
db_manager = DatabaseManager(db_name="employees", connection=connection, cursor=cursor)
db_manager.create_table()
employees = get_data("employees_data.json")
db_manager.fill_table(employees_data=employees)
db_manager.get_employees_high_salary(50000)
db_manager.update_employee_salary(name="Иван", salary=60000)
db_manager.delete_employee(name="Анна")
db_connector.close_connection()
