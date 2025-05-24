# GetReport

Инструмент для создания отчетов на основе данных о сотрудниках, хранящихся в файлах CSV.

## 📚 Описание проекта

Консольное приложение для считывания данных из CSV файлов, нормализации этих данных и генерирования отчетов.

## 🚀 Использование

1. Установка:
`git clone https://github.com/RuslanAcharaev/GetReport.git`

2. Перед запуском убедитесь, что у вас установлен:
**Python 3.10+**

3. Запуск:
`python main.py data1.csv data2.csv --report payout`

## 🛠️Доступные аргументы
| Аргумент | Описание | Обязательный |
|----------|------------|---------|
| `files` |  Один или несколько CSV-файлов или путей к CSV-файлам. Это входные файлы, содержащие данные о сотрудниках. Например: data1.csv data2.csv. | Да |
| `--report` | Указывает тип формируемого отчёта. Доступные варианты определены в словаре REPORTS в файле [core/config.py]. | Да |
| `--format` | Указывает формат выходного файла. Доступные варианты определены в словаре OUTPUTS в файле [core/config.py]. Значение по умолчанию — json. | Нет |
| `--name`, `-n` | Задаёт название файла отчёта. Значение по умолчанию — report. | Нет |
| `--console`, `-c` | Флаг для отключения вывода в консоль. По умолчанию вывод включён. Чтобы отключить его, используйте -c. | Нет |

## 📂 Структура проекта

```
GetReport/
├── core/                    # Основная логика
│   ├── __init__.py
│   ├── config.py            # Настройки отчетов и форматов
│   └── process_args.py      # Обработка аргументов CLI
│
├── data_parser/             # Парсинг и нормализация данных
│   ├── __init__.py
│   ├── normalize.py         # Нормализация CSV-данных
│   └── parse_csv.py         # Парсер CSV-файлов
│
├── error_checkers/          # Проверки ошибок
│   ├── __init__.py
│   ├── check_args.py        # Валидация аргументов
│   └── check_file_paths.py  # Проверка путей к файлам
│
├── output/                  # Форматы вывода
│   ├── __init__.py
│   └── to_json.py           # Генерация JSON-отчета
│
├── reports/                 # Логика отчетов
│   ├── __init__.py
│   └── payout.py            # Отчет по выплатам
│
├── tests/                   # Тесты (pytest)
│
├── data1.csv                # Пример CSV-файла с данными
├── data2.csv                # Пример CSV-файла с данными
├── data3.csv                # Пример CSV-файла с данными
├── main.py                  # Главный скрипт для запуска
└── pytest.ini               # Конфигурация pytest
```

## ⚙️ Конфигурация
Доступные отчеты и форматы настраиваются в core/config.py:
```python
from output import to_json
from reports import generate_payout_report

REPORTS = {
    'payout': generate_payout_report  # Добавьте свои отчеты здесь
}

OUTPUTS = {
    'json': to_json  # Добавьте свои форматы здесь
}
```

## 🧪 Тестирование
Код приложения покрыт тестами, написанными на **pytest**
Запуск тестов производится из основной директории командой:
```
pytest ./tests
```

## 📌 Пример запуска приложения
![Example](https://github.com/user-attachments/assets/6380c667-93dd-4523-91c6-be229f1c38c7)


## 📝 Добавление новых отчётов и форматов
### 1. Добавление нового типа отчёта
Создайте функцию генерации отчёта:
Эта функция будет принимать нормализованные данные на вход и возвращать отчёт. Нормализованные данные передаются в виде списка словарей сотрудников (`list[Employee]`):
```python
class Employee(TypedDict):
    id: str
    email: str
    name: str
    department: str
    hours_worked: int
    hourly_rate: int
```
Разместите эту функцию в новом файле внутри директории reports/ (например, reports/summary.py).

Импортируйте и зарегистрируйте функцию:
В файле core/config.py импортируйте новую функцию генерации отчёта и добавьте её в словарь REPORTS.
```python
# core/config.py
from output import to_json
from reports import generate_payout_report
from reports import generate_summary_report  # импортируйте новую функцию генерации отчёта

REPORTS = {
    'payout': generate_payout_report,
    'summary': generate_summary_report  # добавьте новую функцию генерации отчёта
}

OUTPUTS = {
    'json': to_json
}
```

### 2. Добавление нового формата вывода
Создайте функцию форматирования вывода:
Эта функция будет принимать данные отчёта и имя файла, а затем сохранять отчёт в нужном формате. Разместите её в новом файле внутри директории output/ (например, output/to_txt.py).

Импортируйте и зарегистрируйте функцию:
В файле core/config.py импортируйте новую функцию форматирования и добавьте её в словарь OUTPUTS.
```python
# core/config.py
from output import to_json
from output import to_txt  # импортируйте новую функцию форматирования
from reports import generate_payout_report

REPORTS = {
    'payout': generate_payout_report
}

OUTPUTS = {
    'json': to_json,
    'txt': to_txt  # добавьте новую функцию форматирования
}
```
