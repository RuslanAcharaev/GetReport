from output import to_json
from reports import generate_payout_report

REPORTS = {
    'payout': generate_payout_report
}

OUTPUTS = {
    'json': to_json
}