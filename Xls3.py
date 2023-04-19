import csv

# Read in the spreadsheet data
with open('your_spreadsheet.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = [row for row in reader]

# Calculate failure count and total checks
failures = [row for row in rows if row['Mandatory Control'] == '0' and row['Sub Control ID'] == '0']
failure_count = {}
for row in failures:
    key = (row['Dashboard Family'], row['Mandatory Control'], row['Sub Control ID'], row['Subcontrol'])
    failure_count[key] = failure_count.get(key, 0) + 1
failure_count = [{'Dashboard Family': key[0], 'Mandatory Control': key[1], 'Sub Control ID': key[2], 'Subcontrol': key[3], 'failure count': value} for key, value in failure_count.items()]

total_checks = {}
for row in rows:
    key = (row['Dashboard Family'], row['Mandatory Control'], row['Sub Control ID'], row['Subcontrol'])
    total_checks[key] = total_checks.get(key, 0) + 1
total_checks = [{'Dashboard Family': key[0], 'Mandatory Control': key[1], 'Sub Control ID': key[2], 'Subcontrol': key[3], 'total checks': value} for key, value in total_checks.items()]

# Merge failure count and total checks data
report_data = []
for f in failure_count:
    for t in total_checks:
        if f['Dashboard Family'] == t['Dashboard Family'] and f['Mandatory Control'] == t['Mandatory Control'] and f['Sub Control ID'] == t['Sub Control ID'] and f['Subcontrol'] == t['Subcontrol']:
            report_data.append({**f, **t})
            break

# Write output to new spreadsheet file
with open('output_spreadsheet.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Dashboard Family', 'Mandatory Control', 'Sub Control ID', 'Subcontrol', 'failure count', 'total checks'])
    writer.writeheader()
    writer.writerows(report_data)
