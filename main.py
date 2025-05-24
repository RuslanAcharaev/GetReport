import argparse

from core import process_args, REPORTS, OUTPUTS


def main():
    parser = argparse.ArgumentParser(
        description='Генератор отчетов по заработной плате сотрудников. '
                    'Позволяет создавать различные отчеты на основе CSV-файлов с данными.'
    )
    parser.add_argument(
        'files',
        metavar='FILE',
        type=str,
        nargs='+',
        help='Один или несколько CSV-файлов с данными сотрудников. '
             'Можно указать через пробел несколько файлов или пути к ним.'
    )
    parser.add_argument(
        '--report',
        type=str,
        required=True,
        choices=REPORTS.keys(),
        help='Тип генерируемого отчета. Доступные варианты: '
             f'{", ".join(REPORTS.keys())}.'
    )
    parser.add_argument(
        '--format',
        type=str,
        default='json',
        choices=OUTPUTS.keys(),
        help='Формат выходного файла отчета. По умолчанию: json. '
             f'Доступные форматы: {", ".join(OUTPUTS.keys())}.'
    )
    parser.add_argument(
        '-n', '--name',
        type=str,
        default='report',
        help='Базовое название для выходного файла (без расширения). '
             'По умолчанию: "report".'
    )
    parser.add_argument(
        '-c', '--console',
        action="store_false",
        default=True,
        help='Отключает вывод отчета в консоль. '
             'По умолчанию отчет выводится и в файл, и в консоль. '
             'Если указан этот флаг, вывод будет только в файл.'
    )

    process_args(parser.parse_args())

    return 0


if __name__ == '__main__':
    main()
