import os
import json
from output import to_json


def test_to_json(tmp_path):
    os.chdir(tmp_path)

    test_data = {'Marketing': {'employees': [
        {'name': 'Alice Johnson', 'hours': 160, 'rate': 50, 'payout': 8000}
    ], 'total_hours': 310, 'total_payout': 13250}}
    filename = "test_report.json"

    to_json(test_data, filename)

    assert os.path.exists(filename)

    with open(filename, 'r') as f:
        content = json.load(f)

    assert content == test_data


def test_to_json_filename(tmp_path):
    os.chdir(tmp_path)

    test_data = {'Marketing': {'employees': [
        {'name': 'Alice Johnson', 'hours': 160, 'rate': 50, 'payout': 8000}
    ], 'total_hours': 310, 'total_payout': 13250}}
    filename = "test_report"

    to_json(test_data, filename)

    assert os.path.exists("test_report.json")

    with open("test_report.json", 'r') as f:
        content = json.load(f)

    assert content == test_data
