import json


def to_json(report: dict, filename='report.json') -> None:
    if not filename.endswith('.json'):
        filename += '.json'
    with open(filename, 'w') as f:
        json.dump(report, f, indent=4)
