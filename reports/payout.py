from typing import TypedDict


class Employee(TypedDict):
    name: str
    hours: int
    rate: int
    payout: int


class Department(TypedDict):
    employees: list[Employee]
    total_hours: int
    total_payout: int


def generate_payout_report(data: list[dict[str, str | int]], console: bool = True) -> dict[str, Department]:
    report = {}

    for employee in data:
        department = employee['department']
        hours_worked = employee['hours_worked']
        hourly_rate = employee['hourly_rate']
        payout = hours_worked * hourly_rate

        report.setdefault(department, {
            'employees': [],
            'total_hours': 0,
            'total_payout': 0
        })

        report[department]['employees'].append({
            'name': employee['name'],
            'hours': hours_worked,
            'rate': hourly_rate,
            'payout': payout
        })
        report[department]['total_hours'] += hours_worked
        report[department]['total_payout'] += payout

    if console:
        print_payout_report(report)
    return report


def print_payout_report(report: dict[str, Department]) -> None:
    if not report:
        return
    headers = {'department': 15, 'name': 20, 'hours': 8, 'rate': 6, 'payout': 10}

    print(f"{'department':<{headers['department']}} "
          f"{'name':<{headers['name']}} "
          f"{'hours':<{headers['hours']}} "
          f"{'rate':<{headers['rate']}} "
          f"{'payout':<{headers['payout']}}")
    print()

    for department, data in report.items():
        print(f"{department:<{headers['department']}}")

        for employee in data['employees']:
            print(f"{'-' * 14:<{headers['department']}} "
                  f"{employee['name']:<{headers['name']}} "
                  f"{employee['hours']:<{headers['hours']}} "
                  f"{employee['rate']:<{headers['rate']}} "
                  f"${employee['payout']:<{headers['payout'] - 1}}")

        print(f"{(headers['department'] + headers['name'] + 2) * ' '}"
              f"{data['total_hours']:<{headers['hours']}} "
              f"{(headers['rate']) * ' '} "
              f"${data['total_payout']}")
        print()
