from unittest.mock import patch

from error_checkers import check_files


def test_check_existing_file_paths(tmp_path):
    file1 = tmp_path / "file1.csv"
    file1.write_text("test content")
    file2 = tmp_path / "file2.csv"
    file2.write_text("test content")

    assert check_files([str(file1), str(file2)]) == True


def test_check_non_existing_file_paths(tmp_path):
    non_existing_files = ['non_existing_file1.csv', 'non_existing_file2.csv']

    assert check_files(non_existing_files) == False


def test_check_mixed_file_paths(tmp_path):
    file1 = tmp_path / "file1.csv"
    file1.write_text("test content")

    assert check_files([str(file1), 'non_existing_file2.csv']) == False


@patch('os.path.exists')
def test_check_files_unexpected_error(mock_exists):
    mock_exists.side_effect = Exception("Неожиданная ошибка при чтении файлов")
    assert check_files(['some_file.csv']) == False
