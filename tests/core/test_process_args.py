from types import SimpleNamespace

from core import process_args


def test_process_args(tmp_path):
    file1 = tmp_path / "file1.csv"
    file1.write_text("id,email,name,department,hours_worked,hourly_rate\n"
                     "1,alice@example.com,Alice Johnson,Marketing,160,50\n")
    args = SimpleNamespace(files=[file1], report='payout', format='json', name='report', console=True)

    result = process_args(args)
    assert result == 0


def test_process_args_invalid_report(tmp_path):
    file1 = tmp_path / "file1.csv"
    file1.write_text("id,email,name,department,hours_worked,hourly_rate\n"
                     "1,alice@example.com,Alice Johnson,Marketing,160,50\n")
    args = SimpleNamespace(files=[file1], report='invalid', format='json', name='report', console=True)

    result = process_args(args)
    assert result == 1
