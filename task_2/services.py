from typing import Any

data = [
    {"name": "Иван", "position": "разработчик", "salary": 55000},
    {"name": "Анна", "position": "аналитик", "salary": 48000},
    {"name": "Петр", "position": "тестировщик", "salary": 52000},
]


def filter_employee_by_salary(employees: list[dict[str, Any]],salary: int) -> list[str]:
    return [x["name"] for x in employees if x["salary"] > salary]

def avg_salary(employees: list[dict[str, Any]]) -> float:
    total_salary = sum([x["salary"] for x in employees])
    return round(total_salary / len(employees), 2)

def filter_all_by_salary(employees: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(employees, key=lambda x: x["salary"], reverse=True)

