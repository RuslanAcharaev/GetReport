def parse_csv_files(file_paths: list[str]) -> list[dict[str, str]]:
    raw_data = []

    for file_path in file_paths:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            if not lines:
                continue

            headers = [h.strip() for h in lines[0].split(',')]
            for line in lines[1:]:
                values = [v.strip() for v in line.split(',')]
                employee = dict(zip(headers, values))
                raw_data.append(employee)

    return raw_data
