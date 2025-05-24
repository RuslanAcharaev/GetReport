from types import SimpleNamespace
from error_checkers import check_args


def test_check_args_valid():
    args = SimpleNamespace(report='payout', format='json')
    assert check_args(args) == True


def test_check_args_invalid_report():
    args = SimpleNamespace(report='invalid_report', format='json')
    assert check_args(args) == False


def test_check_args_invalid_format():
    args = SimpleNamespace(report='payout', format='invalid_format')
    assert check_args(args) == False
