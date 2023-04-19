import csv

# Open the CSV file and read its contents into a list of dictionaries
with open('input.csv', 'r', encoding='utf8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Create dictionaries to hold the failure and total check counts
failure_count = {}
total_checks = {}

# Iterate over the rows and update the failure and total check counts
for row in rows:
    if row['Subcontrol'] != '':
        key = (row['Dashboard Family'], row['Mandatory Control'], row['Subcontrol'], row['Rule Name'])
        failure = row['checkstatus'] == '0'
        count = failure_count.get(key, 0)
        failure_count[key] = count + failure
        count = total_checks.get(key, 0)
        total_checks[key] = count + 1

# Write the output to a new CSV file
with open('output.csv', 'w', newline='', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerow(['Dashboard Family', 'Mandatory Control', 'Subcontrol', 'Rule Name', 'Failure Count', 'Total Checks'])
    for key in sorted(failure_count.keys()):
        dashboard_family, mandatory_control, subcontrol, rule_name = key
        failure_count_val = failure_count.get(key, 0)
        total_checks_val = total_checks.get((dashboard_family, mandatory_control, subcontrol, ''), 0)
        writer.writerow([dashboard_family, mandatory_control, subcontrol, rule_name, failure_count_val, total_checks_val])
