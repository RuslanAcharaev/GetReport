from data_parser import parse_csv_files


def test_parse_csv_files(tmp_path):
    file1 = tmp_path / "file1.csv"
    file1.write_text("id,email,name,department,hours_worked,hourly_rate\n"
                     "1,alice@example.com,Alice Johnson,Marketing,160,50\n")
    file2 = tmp_path / "file2.csv"
    file2.write_text("department,id,email,name,hours_worked,rate\n"
                     "HR,101,grace@example.com,Grace Lee,160,45\n")
    file3 = tmp_path / "file3.csv"
    file3.write_text("email,name,department,hours_worked,salary,id\n"
                     "karen@example.com,Karen White,Sales,165,50,201\n")

    result = parse_csv_files([str(file1), str(file2), str(file3)])

    assert len(result) == 3

    assert result[0]["id"] == "1"
    assert result[0]["email"] == "alice@example.com"
    assert result[0]["hourly_rate"] == "50"

    assert result[1]["id"] == "101"
    assert result[1]["rate"] == "45"

    assert result[2]["salary"] == "50"
    assert result[2]["id"] == "201"


def test_parse_csv_files_empty_file(tmp_path):
    empty_file = tmp_path / "empty.csv"
    empty_file.write_text("")

    result = parse_csv_files([str(empty_file)])
    assert result == []
