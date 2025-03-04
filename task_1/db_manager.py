from typing import Any

import psycopg2
from psycopg2 import OperationalError


class DatabaseConnector:
    """
    Class for creating connection to database.
    """

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def open_connection(self, db_params: dict[str, Any]):
        try:
            self.connection = psycopg2.connect(**db_params)
            self.cursor = self.connection.cursor()
        except OperationalError as err:
            print(f"The error {err} is occurred.")
        return self.connection, self.cursor

    def close_connection(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()


class DatabaseManager:
    """
    Class for interacting with database.
    """

    def __init__(self, db_name: str, connection, cursor):
        self.db_name = db_name
        self.connection = connection
        self.cursor = cursor

    def create_table(self):
        try:
            self.cursor.execute("""CREATE TABLE employees (
                                       id SERIAL PRIMARY KEY ,
                                       name VARCHAR(100),
                                       position VARCHAR(100),
                                       salary NUMERIC(10, 2))""")
        except OperationalError as err:
            print(f"The error '{err}' occurred")

    def fill_table(self, employees_data: list[dict[str, Any]]):
        for employee in employees_data:
            try:
                self.cursor.execute(
                    f"INSERT INTO employees (name, position, salary)"
                    f"VALUES ('{employee['name']}', '{employee['position']}' , '{employee['salary']}')"
                )
            except OperationalError as err:
                print(f"The error '{err}' occurred")

    def get_employees_high_salary(self, salary: int):
        try:
            self.cursor.execute(
                f"SELECT * FROM employees WHERE salary > {salary} ORDER BY salary DESC"
            )
        except OperationalError as err:
            print(f"The error '{err}' occurred")

        return self.cursor.fetchall()

    def update_employee_salary(self, name: str, salary: int):
        try:
            self.cursor.execute(
                f"UPDATE employees SET salary = {salary} WHERE name = '{name.title()}'"
            )
        except OperationalError as err:
            print(f"The error '{err}' occurred")

    def delete_employee(self, name: str):
        try:
            self.cursor.execute(f"DELETE FROM employees WHERE name = '{name.title()}'")
        except OperationalError as err:
            print(f"The error '{err}' occurred")
