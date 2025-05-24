import argparse

from core import process_args, REPORTS, OUTPUTS


def main():
    parser = argparse.ArgumentParser(description='Генерирует отчеты по данным сотрудников')
    parser.add_argument('files', metavar='FILE', type=str, nargs='+',
                        help='CSV файлы или пути к CSV файлам')
    parser.add_argument('--report', type=str, required=True,
                        choices=REPORTS.keys(),
                        help='Тип отчета для генерации')
    parser.add_argument('--format', type=str, default='json',
                        choices=OUTPUTS.keys(),
                        help='Формат файла для отчета')
    parser.add_argument('-n', type=str, default='report',
                        help='Название файла отчета')
    parser.add_argument('-c', action="store_false", default=True,
                        help="Отключить вывод в консоль (по умолчанию: вывод включён)"
                        )

    process_args(parser.parse_args())

    return 0


if __name__ == '__main__':
    main()
