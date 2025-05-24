from reports import generate_payout_report, print_payout_report

test_data = [
    {'id': '1', 'email': 'alice@example.com', 'name': 'Alice Johnson', 'department': 'Marketing',
     'hours_worked': 160, 'hourly_rate': 50},
    {'id': '102', 'email': 'henry @ example.com', 'name': 'Henry Martin', 'department': 'Marketing',
     'hours_worked': 150, 'hourly_rate': 35},
    {'id': '101', 'email': 'grace@example.com', 'name': 'Grace Lee', 'department': 'HR',
     'hours_worked': 160, 'hourly_rate': 45}
]


def test_generate_payout_report():
    result = generate_payout_report(test_data, console=False)

    assert set(result.keys()) == {'Marketing', 'HR'}
    assert len(result['Marketing']['employees']) == 2
    assert len(result['HR']['employees']) == 1

    assert result['Marketing']['total_hours'] == 310
    assert result['Marketing']['total_payout'] == 13250
    assert result['HR']['total_payout'] == 7200


def test_generate_payout_report_empty_data():
    result = generate_payout_report([], console=False)
    assert result == {}


def test_generate_and_print_payout_report(capsys):
    result = generate_payout_report(test_data)

    captured = capsys.readouterr()
    output = captured.out

    assert 'Marketing' in output
    assert 'HR' in output
    assert 'Henry Martin' in output
    assert 'Grace Lee' in output
    assert '13250' in output


def test_generate_and_print_payout_report_empty_data(capsys):
    result = generate_payout_report([])

    captured = capsys.readouterr()
    assert captured.out == ''
