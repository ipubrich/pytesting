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
        if row['checkstatus'] in ['0', '1']:
            check_key = (row['Dashboard Family'], row['Mandatory Control'], row['Sub Control ID'], row['Rule Name'])
            count = total_checks.get(check_key, 0)
            total_checks[check_key] = count + 1

# Write the output to a new CSV file
with open('output.csv', 'w', newline='', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerow(['Dashboard Family', 'Mandatory Control', 'Sub Control ID', 'Subcontrol', 'Rule Name', 'Failure Count', 'Total Checks'])
    for key in sorted(failure_count.keys()):
        dashboard_family, mandatory_control, subcontrol, rule_name = key
        failure_count_val = failure_count.get(key, 0)
        total_checks_key = (dashboard_family, mandatory_control, subcontrol, rule_name)
        total_checks_val = total_checks.get(total_checks_key, 0)
        writer.writerow([dashboard_family, mandatory_control, subcontrol, sub_control_id, rule_name, failure_count_val, total_checks_val])
