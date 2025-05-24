from core import REPORTS, OUTPUTS
from data_parser import parse_csv_files, normalize_data
from error_checkers import check_files, check_args


def process_args(args):
    if check_args(args) and check_files(args.files):
        raw_data = parse_csv_files(args.files)
        normalized_data = normalize_data(raw_data)
        report_generator = REPORTS.get(args.report)
        report = report_generator(normalized_data, args.console)
        formatter = OUTPUTS.get(args.format)
        formatter(report, args.name)
        return 0
    return 1
