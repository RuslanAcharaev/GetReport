from core import REPORTS, OUTPUTS


def check_args(args):
    try:
        report_generator = REPORTS.get(args.report)
        if not report_generator:
            raise ValueError(f"Неизвестный тип отчета: {args.report}")
        formatter = OUTPUTS.get(args.format)
        if not formatter:
            raise ValueError(f"Неизвестный формат вывода: {args.format}")
    except ValueError as e:
        print(f"Ошибка: {e}")
        return False
    return True