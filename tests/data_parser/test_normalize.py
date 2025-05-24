from data_parser import normalize_data


def test_normalize_data():
    input_data = [
        {
            "id": "1",
            "email": "alice@example.com",
            "name": "Alice Johnson",
            "department": "Marketing",
            "hours_worked": "160",
            "hourly_rate": "50"
        },
        {
            "id": "2",
            "email": "bob@example.com",
            "name": "Bob Smith",
            "department": "Sales",
            "hours_worked": "150",
            "rate": "40"
        },
        {
            "id": "3",
            "email": "carol@example.com",
            "name": "Carol Williams",
            "department": "HR",
            "hours_worked": "170",
            "salary": "60"
        }
    ]

    result = normalize_data(input_data)

    assert len(result) == 3

    assert result[0]["id"] == "1"
    assert result[0]["hours_worked"] == 160
    assert result[0]["hourly_rate"] == 50

    assert result[1]["hourly_rate"] == 40
    assert result[1]["hours_worked"] == 150

    assert result[2]["hourly_rate"] == 60
    assert result[2]["hours_worked"] == 170


def test_normalize_data_empty_input():
    result = normalize_data([])
    assert result == []


def test_normalize_data_missing_values():
    input_data = [{
        "id": "1",
    }]

    result = normalize_data(input_data)

    assert result[0]["hours_worked"] == 0
    assert result[0]["hourly_rate"] == 0
    assert result[0]["email"] == ""
    assert result[0]["name"] == ""
    assert result[0]["department"] == ""
