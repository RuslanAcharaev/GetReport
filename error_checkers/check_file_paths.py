import os


def check_files(file_paths):
    try:
        for file_path in file_paths:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Файл не найден: {file_path}")
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        return False
    except Exception as e:
        print(f"Неожиданная ошибка при чтении файлов: {e}")
        return False
    return True