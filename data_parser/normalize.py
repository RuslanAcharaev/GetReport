from typing import TypedDict


class Employee(TypedDict):
    id: str
    email: str
    name: str
    department: str
    hours_worked: int
    hourly_rate: int


def normalize_data(data: list[dict[str, str]]) -> list[Employee]:
    normalized = []
    rate_variants = ['hourly_rate', 'rate', 'salary']
    for employee in data:
        hourly_rate = '0'
        for variant in rate_variants:
            if variant in employee:
                hourly_rate = employee.get(variant, '0')

        normalized_info = {
            'id': employee.get('id', ''),
            'email': employee.get('email', ''),
            'name': employee.get('name', ''),
            'department': employee.get('department', ''),
            'hours_worked': int(employee.get('hours_worked', '0')),
            'hourly_rate': int(hourly_rate),
        }

        normalized.append(normalized_info)

    return normalized
